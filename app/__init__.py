from . import *

# automatically registers all the entities to data store


from app import entities
from app.entities.base import BaseEntity
from types import ModuleType
from app.datastore import DataStore

for name, cls in entities.__dict__.items():
    if isinstance(cls, ModuleType) and name != 'app.entities.base':
        for inner_name, inner_cls in cls.__dict__.items():
            try:
                if issubclass(inner_cls, BaseEntity) and inner_name != 'BaseEntity':
                    DataStore.register_entity(inner_cls)
            except TypeError as e:
                pass