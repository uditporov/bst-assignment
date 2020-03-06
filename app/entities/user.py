from uuid import uuid4
from app.exceptions import RoleAlreadyExists, RoleDoesnotExists


USERS = {}


class User(object):
    id = None
    name = None

    # stores all the roles that this particular user have, id of the roles is store here only
    roles = []

    # internal pre-calculate HashMap that holds whether the particular Resource+Operations is accessible or not
    _accessible_ops = {}

    def __init__(self, name=None):
        self.name = name

    def save(self):
        self.id = uuid4()
        USERS[self.id] = self

    def add_role(self, role):
        if role in self.roles:
            raise RoleAlreadyExists("This role is already assigned to this user.")
        self.roles.append(role)

    def remove_role(self, role):
        if role not in self.roles:
            raise RoleAlreadyExists("This role is not assigned to this user.")
        self.roles.remove(role)
