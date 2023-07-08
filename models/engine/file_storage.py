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
        """ new func """
        cname = obj.__class__.__name__
        value = obj.id
        keyname = f"{cname}.{value}"
        self.__objects[keyname] = obj

    def save(self):
        """ save func """
        serialized_data = {}
        for key, value in self.__objects.items():
            serialized_data[key] = value.to_dict()
        with open(self.__file_path, 'w') as o_file:
            json.dump(serialized_data, o_file)

    def reload(self):
        """ reload func """
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r", encoding="utf-8") as i_file:
                for key, value in json.load(i_file).items():
                    value = BaseModel(**value)
                    self.__objects[key] = value
        except Exception:
            pass
