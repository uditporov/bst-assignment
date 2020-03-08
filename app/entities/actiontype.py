from app.entities.base import BaseEntity


class ActionType(BaseEntity):
    name = None

    def __init__(self, name=None):
        self.name = name
        super().__init__()

    def __str__(self):
        return self.name
