#!/usr/bin/python3
""" file storage """
import json


class FileStorage():
    """ file storage class """

    def __init__(self):
        """ initialization """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ self func """
        return self.__objects

    def new(self, obj):
        """ New func """
        cname = obj.__class__.__name__
        value = obj.id
        keyname = f"{cname}.{value}"
        self.__objects[keyname] = obj.to_dict()

    def save(self):
        """ Save func """

        with open(self.__file_path, 'w') as o_file:
            o_file.write(json.dumps(self.__objects))

    def reload(self):
        """ reload func """
        try:
            with open(self.__file_path, "r", encoding="UTF8") as i_file:
                for key, value in json.load(i_file).items():
                    self.__objects[key] = value
        except Exception:
            pass
