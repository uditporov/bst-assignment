from uuid import uuid4
from app.datastore import DataStore


class BaseEntity(object):
    """
    Base class for all entities. Just inherit this class, it automatically adds id attribute to the entity.
    ~ automatically manages the value of id.
    ~ provide default methods to create, update, delete and read the values.
    ~ Manages all the interaction with data storage using DataStore class

    """

    # autogenerated id for the entities, keeps the uuid
    id = None

    def __init__(self):
        pass

    def save(self):
        """
        Generates the id for the entity if not present and save it to the data store
        :return:
        """
        if not self.id:
            self.id = uuid4()
        DataStore.add_instance(self)

    def delete(self):
        """
        Deletes the entity from the data store
        :return:
        """
        self.id = uuid4()
        DataStore.remove_instance(self)

    @classmethod
    def get(cls, _id):
        """
        Can be used to fetch a particular entity by id from the data store
        :param _id:
        :return:
        """
        return DataStore.get_instance(cls, _id)

    @classmethod
    def get_all(cls):
        """
        Returns all the instances of a particular entity
        :return:
        """
        return DataStore.get_all_instance(cls)
