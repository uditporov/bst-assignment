from app.entities import User, Resource, Role, ActionType


class Menu(object):
    main_action_map = [
        'login_as_another_user',
        'access_resource',
        'assign_role',
        'remove_role',
        'list_roles'
    ]

    def __init__(self, logged_in):
        self.logged_in = logged_in

    @staticmethod
    def take_user_input(message, min_val, max_val):
        while True:
            try:
                value = input(message)
                value = int(value)
                if max_val >= value >= min_val:
                    break

            except TypeError as e:
                pass

            print("Incorrect selection, press enter to try again")
            input()

        return value

    def render(self):
        while True:
            self._render_main_menu()
            value = Menu.take_user_input("Your choice -", 1, len(Menu.main_action_map))
            getattr(self, self.main_action_map[value-1])()

    def login_as_another_user(self):
        users = User.get_all()
        for user in users:
            if user.id != self.logged_in.id:
                self.logged_in = user
                break

    def access_resource(self):
        resource_chosen = self._take_entity_input(Resource)
        action_type_chosen = self._take_entity_input(ActionType)

        if self.logged_in.is_operation_allowed(resource_chosen, action_type_chosen):
            print("You are allowed to perform this operation")
        else:
            print("You don't have permission to perform this operation")
        input()

    def assign_role(self):
        user_chosen = self._take_entity_input(User)
        role_chosen = self._take_entity_input(Role)

        try:
            user_chosen.add_role(role_chosen)
        except Exception as e:
            print(e)

    def remove_role(self):
        user_chosen = self._take_entity_input(User)
        role_chosen = self._take_entity_input(Role)

        try:
            user_chosen.remove_role(role_chosen)
        except Exception as e:
            print(e)

    def list_roles(self):
        user_chosen = self._take_entity_input(User)
        for role_id in user_chosen.roles:
            print(Role.get(role_id))

    def _render_main_menu(self):
        print("Hi! You are logged in as {}".format(self.logged_in.name))
        print("Press 1 for Login as another user")
        print("Press 2 to access resource")
        print("Press 3 to assign role to a user")
        print("Press 4 to remove role from a user")
        print("Press 5 to list roles of a user")

    def _take_entity_input(self, entity):
        instances = entity.get_all()
        choices = []

        counter = 1
        for instance in instances:
            print("Press {} to select {} - {}".format(str(counter), str(entity.__name__), str(instance)))
            choices.append(instance)
            counter += 1

        value = Menu.take_user_input("Your choice - ", 1, len(choices))
        entity_chosen = choices[value-1]

        return entity_chosen
