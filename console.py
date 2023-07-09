#!/usr/bin/python3

""" console hbnb """

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import re



class HBNBCommand(cmd.Cmd):
    """ cmd hbnb class """

    prompt = "(hbnb) "

    class_list = ['BaseModel', 'User', 'State', 'City',
                  'Amenity', 'Place', 'Review']

    def emptyline(self):
        return None

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of <arg>"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.class_list:
            print("** class doesn't exist **")
        else:
            obj = eval(arg)()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class \
name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            keyname = f"{args[0]}.{args[1]}"
            database = storage.all()
            if keyname in database:
                print(database[keyname])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            keyname = f"{args[0]}.{args[1]}"
            database = storage.all()
            try:
                database.pop(keyname)
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances \
based or not on the class name"""
        if arg and (arg not in self.class_list):
            print("** class doesn't exist **")
        else:
            database = storage.all()
            myd = []
            if not arg:
                for keyname in database:
                    myd.append(str(database[keyname]))
            else:
                for keyname in database:
                    if keyname.startswith(arg):
                        myd.append(str(database[keyname]))
            print(myd)

    def do_update(self, arg):
        """Updates an instance based on the class name and id \
by adding or updating attribute"""
        args = re.findall(r'\"[^\"]+\"|\S+', arg)
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            keyname = f"{args[0]}.{args[1]}"
            database = storage.all()
            try:
                obj = database[keyname]
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    obj[args[2]] = args[3]
                    storage.save()
            except KeyError:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
