"""
This module consists of all the variable which are used as Data Storage for the application

Author: Udit Porov
Date: 06/03/2020
"""

from app.utils import Singleton


class DataStore(metaclass=Singleton):
    """
    It holds all the data of the application.
    Each entity has its own HashMap, which store the data with key as ID(hex) and value as entity object
    """

    @staticmethod
    def register_entity(entity_class):
        """
        All the entity must be registered with the data store first, which creates a hashmap which store all the
        data for that particular entity
        :param entity_class:
        :return:
        """
        if not hasattr(DataStore, entity_class.__name__):
            setattr(DataStore, entity_class.__name__, dict())

    @staticmethod
    def add_instance(instance):
        """
        Saves/adds new instance to the data store for a particular entity
        :param instance:
        :return:
        """
        data_store = getattr(DataStore, type(instance).__name__)
        data_store[instance.id] = instance

    @staticmethod
    def remove_instance(instance):
        """
        Deletes a particular instance from the data store of a particular entity
        :param instance:
        :return:
        """
        data_store = getattr(DataStore, type(instance).__name__)
        del data_store[instance.id]

    @staticmethod
    def get_instance(entity_class, _id):
        """
        Return a particular instance of a entity using the id attribute
        :param entity_class:
        :param _id:
        :return:
        """
        data_store = getattr(DataStore, entity_class.__name__)
        return data_store[_id]

    @staticmethod
    def get_all_instance(entity_class):
        """
        Returns all the instances of a entity
        :param entity_class:
        :return:
        """
        data_store = getattr(DataStore, entity_class.__name__)
        return data_store.values()
