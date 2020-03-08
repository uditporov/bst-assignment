from app.entities.base import BaseEntity
from app.utils import get_operation_identifier


class Role(BaseEntity):
    name = None

    def __init__(self, name=None):
        self.name = name

        # holds the list of ActionType + Resource (operations), saved as tuple (Resource.id, ActionType.id)
        self.allowed_operations = set()

        # internal attribute, that holds reverse mapping of users with this particular role for performance optimization
        self._users = set()

        super().__init__()

    # ##custom operations for role entity## #

    def bulk_add_allowed_operations(self, operations):
        """
        Adds multiple operations to a particular Role
        ~ Post that updates those operation's permission to Users
        :param operations: List of operations, each operation is a surrogate key with (Resource.id, ActionType.id)
        :return:
        """
        self.allowed_operations.update(operations)
        self.sync_all_users_operations()

    def add_allowed_operations(self, resource, action_type):
        """
        Adds one operations at a time to the particular role
        ~ Post that updates those operation's permission to Users
        :param resource: Resource entity
        :param action_type: ActionType entity
        :return:
        """
        operation_id = get_operation_identifier(resource, action_type)
        self.allowed_operations.add(operation_id)

        from app.entities.user import User

        # update all the user's pre calculate permissions
        for user_id in self._users:
            user = User.get(user_id)
            user.add_accessible_ops(operation_id)

    def remove_allowed_operations(self, resource, action_type):
        """
        Removes a particular operations from a Role
        :param resource: Resource entity
        :param action_type: ActionType entity
        :return:
        """
        operation_id = get_operation_identifier(resource, action_type)
        self.allowed_operations.remove(get_operation_identifier(resource, action_type))

        from app.entities.user import User

        # update all the user's pre calculate permissions
        for user_id in self._users:
            user = User.get(user_id)
            user.remove_accessible_ops(operation_id)

    def add_user(self, user):
        self._users.add(user.id)

    def remove_user(self, user):
        self._users.remove(user.id)

    def sync_all_users_operations(self):
        from app.entities.user import User

        # update all the user's pre calculate permissions
        for user_id in self._users:
            user = User.get(user_id)
            user.sync_accessible_ops()
