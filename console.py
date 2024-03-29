#!/usr/bin/python3
"""
Module defines the entry point of the command interpreter

DESCRIPTION
-----------

This defines a class HBNBcommand() that inherits from cmd.Cmd class.
cmd.Cmd class provides us with an abstractions that allows us to create
a powerful command line interpreter.

This interpreter/console allows us to manipulate a powerful storage system
of files through the use of commands.

The commands implemented include:
  a) create - creates a new instance
  b) show - prints string representation of an instance
  c) destroy - deletes an instance
  d) all - prints string representation of all instances
  e) update - updates an instance


USAGE
-----
  $ ./console.py
  (hbnb) help

  Documented commands (type help <topic>):
  ========================================
  EOF  all  create  destroy  help  quit  show  update

  (hbnb) help quit
  Quit command to exit the program

  (hbnb)
  (hbnb) quit
  $
"""

import re
import cmd
import json
import models
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel

# create list of class names
class_list = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """
    defines command line interpreter
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Overrides the default behaviour by doing nothing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Builtin EOF command to gracefully catch error."""
        return True

    def do_create(self, arg):
        """
        Creates an instance of BaseModel, saves it to JSON file
        and then prints its id to stdout.
        """
        # split arg into list of strings
        args = arg.split()
        # validate the class name
        if not validate_classname(args):
            return

        # create object
        obj = class_list[args[0]]()

        if len(args) > 1:
            for param in args[1:]:
                k, v = param.split('=')
                # validate input data
                if is_int(v):
                    value = int(v)
                elif is_float(v):
                    value = float(v)
                else:
                    # string validation
                    if v.startswith('"'):
                        # Escape double quotes in string
                        v = v.replace('"', '\"')
                        # Replace underscore with a space
                        v = v.replace('_', ' ')
                        # Replace opening double quotes with single quotes
                        value = v.replace('"', "", 1)
                        # Replace cosing double quotes with single quotes
                        value = value[::-1].replace('"', "", 1)[::-1]
                    else:
                        return
                # set attribute to object
                setattr(obj, k, value)

        # save object
        obj.save()

        print(obj.id)

    def do_show(self, arg):
        """
        Prints the string represenatation of an instance
        based on class name and id
        """
        args = arg.split()
        if not validate_classname(args, True):
            return

        # get the obj dict
        obj_dict = models.storage.all()
        # create a key to search
        key = "{}.{}".format(args[0], args[1])
        # search for the object instance
        if key not in obj_dict.keys():
            print("** no instance found **")
        else:
            value = obj_dict[key]
            print(value)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name
        and id then save changes to JSON file
        """
        args = arg.split()
        if not validate_classname(args, True):
            return
        # get the obj dict
        obj_dict = models.storage.all()
        # create a key to search
        key = "{}.{}".format(args[0], args[1])
        # search for the object instance
        if key not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict[key]
            models.storage.save()

    def do_all(self, arg):
        """
        Prints all string represenatation of all instances based
        or not of the class name.
        """
        # create a list of args
        args = arg.split()
        # get the list of instances stored in file
        obj_dict = models.storage.all()

        # print all instances if class name not provided
        if len(args) == 0:
            print(["{}".format(str(val)) for val in obj_dict.values()])
        else:
            if args[0] not in class_list.keys():
                print("** class doesn't exist **")
            else:
                print(["{}".format(str(val)) for val in obj_dict.values()
                       if type(val).__name__ == args[0]])

    def do_update(self, arg):
        """
        Update an instance based on the class name and id
        by adding or updating attribute then save changes to JSON
        """
        # create list of args
        args = arg.split(maxsplit=3)
        # validate classname and attributes
        if not validate_classname(args, check_id=True):
            return
        if not validate_attributes(args):
            return

        # get list of instances stored
        obj_dict = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in obj_dict.keys():
            print("** no instance found **")
        else:
            # get key instance
            obj_instance = obj_dict[key]
            # cast values to correct types
            value = parse_str(args[3])
            # update/add attribute to instance
            setattr(obj_instance, args[2], value)
            # save to JSON file
            models.storage.save()


# HELPER FUNCTIONS


def validate_classname(args, check_id=False):
    if len(args) == 0:
        print("** class name missing **")
        return False
    if args[0] not in class_list.keys():
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return False
    return True


def validate_attributes(args):
    """Validates the attributes parsed as command argument"""
    if len(args) < 3:
        print("** attribute name missing **")
        return False
    if len(args) < 4:
        print("** value missing **")
        return False
    return True


def is_float(val):
    """Checks if 'val' is float.
    """
    try:
        x = float(val)
    except (TypeError, ValueError):
        return False
    else:
        return True


def is_int(val):
    """Checks if val is int.
    """
    try:
        a = float(val)
        b = int(val)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


def parse_str(arg):
    """Parse `arg` to an `int`, `float` or `string`.
    """
    # remove quotes around atrribute value
    str = re.sub(r"\"", "", arg)
    str = re.sub("'", "", str)

    if is_int(str):
        return int(str)
    elif is_float(str):
        return float(str)
    else:
        return str


if __name__ == "__main__":
    HBNBCommand().cmdloop()
