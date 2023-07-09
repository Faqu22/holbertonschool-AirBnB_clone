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
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ save func """
        myd = {}
        for key in FileStorage.__objects:
            myd[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as o_file:
            o_file.write(json.dumps(myd))

    def reload(self):
        """ reload func """
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF8") as i_file:
                readed = json.load(i_file) if not None else []
                for key, value in readed.items():
                    objcls = readed[key]['__class__']
                    if objcls in FileStorage.cls.keys():
                        FileStorage.__objects[key] = self.cls[objcls](**value)
        except FileNotFoundError:
            pass
