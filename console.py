#!/usr/bin/python3
"""Defines the HBNB console"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = slpit(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBNB interpreter
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        """init method"""
        super().__init__(completekey, stdin, stdout)

    def emptyline(self):
        """do nothing"""
        pass

    def default(self, arg):
        """Default behaviour of cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match is not None:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(arg1[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def do_create(self, args):
        """Usage: create <class> <key 1>=<value> ...
        create a new class instance and prints its id"""
        obj = None
        if args == 'BaseModel':
            obj = BaseModel()
        elif args == 'User':
            obj = User()
        elif args == 'State':
            obj == State()
        if obj is not None:
            print(obj.id)
        else:
            print("** class name doesn't exit **")

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
                for length in models.storage.all().values():
                    if type(length) == model:
                        resp.append(l.__str__())
                print(resp)
            except Exception as e:
                print(e)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of given class"""
        arg1 = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg1[0] == obj.__class__.__name__:
                count += 1
        print(count)

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
