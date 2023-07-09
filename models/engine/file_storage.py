#!/usr/bin/python3
""" file storage """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """ file storage class """

    cls = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
           'Amenity': Amenity, 'Place': Place, 'Review': Review}
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ self func """
        return FileStorage.__objects

    def new(self, obj):
        """ new func """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """ save func """


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
