from app import *
from app.entities import User, Role, Resource, ActionType
from app.utils import get_operation_identifier


def load_initial_data():

    # create default action types
    create_action = ActionType("CREATE")
    create_action.save()

    delete_action = ActionType("DELETE")
    delete_action.save()

    update_action = ActionType("UPDATE")
    update_action.save()

    read_action = ActionType("READ")
    read_action.save()

    # create default resources
    people_resource = Resource("People")
    people_resource.save()

    product_resource = Resource("Product")
    product_resource.save()

    # create users
    user1 = User("User1")
    user1.save()

    admin = User("Admin")
    admin.save()

    # create roles
    admin_role = Role("admin-role")
    admin_operations = set()
    for resource in Resource.get_all():
        for action_type in ActionType.get_all():
            admin_operations.add(get_operation_identifier(resource, action_type))
    admin_role.bulk_add_allowed_operations(admin_operations)
    admin_role.save()

    read_role = Role("read-role")
    read_operations = set()
    for resource in Resource.get_all():
        read_operations.add(get_operation_identifier(resource, read_action))
    read_role.bulk_add_allowed_operations(read_operations)
    read_role.save()

    # assign roles to users
    admin.add_role(admin_role)
    user1.add_role(read_role)


