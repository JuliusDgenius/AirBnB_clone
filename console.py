#!/usr/bin/python3
import cmd
import models
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    __classes = ['BaseModel']

    def emptyline(self):
        """do nothing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def do_create(self, args):
        """Usage: create <class> <key 1>=<value> ...
        create a new cls instance with given keys/values and prints its id"""
        d_list = args.split()
        if not d_list:
            print('** class name missing **')
        elif d_list[0] not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
        else:
            my_object = eval(d_list[0] + '()')

            for i in range(1, len(d_list)):
                result = d_list[i].split('=')
                result[1] = result[1].replace('_', ' ')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
