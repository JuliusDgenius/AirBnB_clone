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
    """Passes command
    Arg:
        Takes any number of arguments
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
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
    intro = "Welcome to the Airbnb console. Type help or ? to list commands.\n"

    prompt = "(hbnb) "
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
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def do_create(self, arg):
        """Usage: create <class>
        create a new class instance and prints its id
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name is missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string rep of a class instance of a given id
        """
        argl = parse(arg)
        obj_dict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """
        Deletes an instance based on clsname and id save changes into the
        JSON file
        """
        argl = parse(arg)
        obj_dict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in oobj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string rep of all instances based on the class name.
        """
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                elif len(argl) == 0:
                    obj1.append(obj.__str__())
            print(obj1)

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
        argl = parse(arg)
        obj_dict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg1) == 4:
            obj = obj_dict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class.__.__dict__.keys():
                valtype = type(obj.__class.__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = obj_dict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
