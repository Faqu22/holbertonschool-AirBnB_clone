#!/usr/bin/python3
""" console hbnb """

import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ cmd hbnb class """

    prompt = "(hbnb) "

    def emptyline(self):
        """ Create a empty line"""
        return ""

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of <arg>"""
        class_list = ['BaseModel', 'FileStorage']
        if not arg:
            print("** class name missing **")
        elif arg not in class_list:
            print("** class doesn't exist **")
        else:
            if arg == 'BaseModel':
                obj = BaseModel()
                obj.save()
                print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class \
name and id"""
        class_list = ['BaseModel', 'FileStorage']
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            keyname = f"{args[0]}.{args[1]}"
            database = storage.all()
            try:
                obj = database[keyname]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        class_list = ['BaseModel', 'FileStorage']
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in class_list:
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
        class_list = ['BaseModel', 'FileStorage']
        if arg and (arg not in class_list):
            print("** class doesn't exist **")
        else:
            database = storage.all()
            if not arg:
                print(database.items())
            else:
                myd = []
                for key in database:
                    if key.startswith(arg):
                        myd.append(database[key])
                print(myd)

    def do_update(self, arg):
        """Updates an instance based on the class name and id \
by adding or updating attribute"""
        class_list = ['BaseModel', 'FileStorage']
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in class_list:
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
