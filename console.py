#!/usr/bin/python3
import cmd
import models
import re
from shlex import split
# from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    __classes = ['BaseModel']

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        """init method"""
        super().__init__(completekey, stdin, stdout)

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

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        `name` and `id`
        """
        if arg == "":
            print('** class name missing **')
            return

        try:
            model.name, model_id = arg.split(' ')
            model = models.storage.find(model_name, model_id)
            print(model.__str__())

        except Exception as e:
            if arg.count(' ') == 0:
                print("** instance id missing **")
            elif arg.count(' ') > 1:
                print("** too many arguments (2 arguments required)**")
            else:
                print(e)

    def do_destroy(self, arg):
        """
        Deletes an instance based on classname and id saving changes into the
        JSON file
        """
        if arg == "":
            print('** class name missing **')
            return

        try:
            model_name, model_id = arg.split(' ')
            models.classes[model_name]  # this checks the model supported
            models.storage.delete(model_name, model_id)
            models.storage.save()

        except Exception as e:

            if arg.count(' ') == 0:
                print('** instance id missing **')
            elif arg.count(' ') > 1:
                print('** too many arguments (2 arguments required)**')
            else:
                print(e)

    def do_all(self, arg):
        """
        Prints all string representation of all instances based on the class
        name.
        """
        if arg == "":
            print([x.__str__() for x in models.storage.all().values()])
        else:
            try:
                model = models.classes[arg]
                resp = []
                for l in models.storage.all().values():
                    if type(l) == model:
                        resp.append(l.__str__())
                print(resp)
            except Exception as e:
                print(e)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the changes into the JSON file)

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if arg == "":
            print('** class name missing **')
            return

        try:
            model_name, model_id, attr, value = arg.split(' ')

            models.storage.update(model_name, model_id, attr, value)
            models.storage.save()

        except Exception as e:
            if arg.count(' ') == 0:
                print('** instance id missing **')
            elif arg.count(' ') == 1:
                print("** attribute name missing **")
            elif arg.count(' ') == 2:
                print('** value missing **')
            elif arg.count(' ') > 3:
                print('** too many arguments (2 arguments required)**')
            else:
                print(e)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
