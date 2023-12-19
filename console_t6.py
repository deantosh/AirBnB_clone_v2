#!/usr/bin/python3
"""
Module defines the entry point of the command interpreter
"""

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    defines command line interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Builtin EOF command to gracefully catch error."""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
