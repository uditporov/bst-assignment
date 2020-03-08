"""
This module hold utilities/helper functions or classes used in this application

Author: Udit Porov
Date: 06/03/2020
"""


class Singleton(type):
    """
    Singleton class which can have only one instance.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def get_operation_identifier(resource, action_type):
    """
    Returns a Surrogate value with the resource and action_type identifier

    :param resource:
    :param action_type:
    :return:
    """
    val = (resource.id, action_type.id)
    return val
