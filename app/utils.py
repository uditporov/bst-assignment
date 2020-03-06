"""
This module hold utilities/helper funtions or classes used in this application

Author: Udit Porov
Date: 06/03/2020
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
