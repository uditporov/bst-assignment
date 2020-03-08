from app.exceptions import RoleAlreadyExists, RoleDoesnotExists
from app.entities.base import BaseEntity
from app.entities.role import Role
from app.utils import get_operation_identifier


class User(BaseEntity):
    name = None

    def __init__(self, name=None):
        self.name = name

        # stores all the roles that this particular user have, id of the roles is store here only
        self.roles = set()

        # internal pre-calculate HashMap that holds whether the particular Resource+Operations is accessible or not
        self._accessible_ops = {}

        super().__init__()

    def __str__(self):
        return self.name

    # ##custom operations for role entity## #

    def add_role(self, role):
        if role.id in self.roles:
            raise RoleAlreadyExists("This role is already assigned to this user.")
        self.roles.add(role.id)

        # update reverse mapping of roles to user
        role.add_user(self)

        self.sync_accessible_ops()

    def remove_role(self, role):
        if role.id not in self.roles:
            raise RoleAlreadyExists("This role is not assigned to this user.")
        self.roles.remove(role.id)

        # update reverse mapping of roles to user
        role.remove_user(self)

        self.sync_accessible_ops()

    def add_accessible_ops(self, operation_id):
        self._accessible_ops[operation_id] = True

    def remove_accessible_ops(self, operation_id):
        self._accessible_ops[operation_id] = False

    def sync_accessible_ops(self):
        self._accessible_ops = dict()
        for role_id in self.roles:
            role = Role.get(role_id)
            for operation in role.allowed_operations:
                self._accessible_ops[operation] = True

    def is_operation_allowed(self, resource, action_type):
        return self._accessible_ops.get(get_operation_identifier(resource, action_type), False)
