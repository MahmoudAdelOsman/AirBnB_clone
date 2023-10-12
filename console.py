#!/usr/bin/env python3
"""module contain notes about cmd class"""
"""function do_update not compleated, needs handling attributes :)"""
import cmd
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Simple command processor for AirBnB_c."""

    prompt = '(hbnb) '

    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    classes_types = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """quit command to exit program\n"""
        print()
        return True

    def do_clear(self, args):
        """clear terminal\n"""
        os.system("clear")

    def do_creat(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes_types:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes_types[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def do_show(self, args):
        """
        Prints the string representation of an instance based on
        the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        new = args.partition(" ")
        my_name = new[0]
        my_id = new[2]
        if not my_name:
            print("** class name missing **")
            return
        elif my_name not in HBNBCommand.classes_types:
            print("** class doesn't exist **")
            return
        elif not my_id:
            print("** instance id missing **")
            return
        key = my_name + "." + my_id
        try:
            all_dict = storage.all()
            print(all_dict[key])
            return
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        new = args.partition(" ")
        my_name = new[0]
        my_id = new[2]
        if not my_name:
            print("** class name missing **")
            return
        elif my_name not in HBNBCommand.classes_types:
            print("** class doesn't exist **")
            return
        elif not my_id:
            print("** instance id missing **")
            return
        key = my_name + "." + my_id
        try:
            all_dict = storage.all()
            del all_dict[key]
            storage.save()
            return
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all instances based
        or not on the class name.
        Ex:     $ all BaseModel
                or
                $ all
        """
        print_list = []

        all_dict = storage.all()
        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes_types:
                print("** class doesn't exist **")
                return
            for k, v in all_dict.items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in all_dict.items():
                print_list.append(str(v))

        print(print_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email \"aibnb@mail.com\".
        Usage: update <class name> <id> <attribute name> \"<attribute value>\"
        """
        new = args.partition(" ")
        my_name = new[0]
        my_id = new[2]
        key = my_name + "." + my_id
        if not my_name:
            print("** class name missing **")
            return
        elif my_name not in HBNBCommand.classes_types:
            print("** class doesn't exist **")
            return
        elif not my_id:
            print("** instance id missing **")
            return
        elif key not in storage.all():
            print("** no instance found **")
            return
        elif not 0:
            print("** attribute name missing **")
            return

    def default(self, line: str):
        print(f"command \"{line}\" not found")

    def emptyline(self):
        """when pressing enter nothing happens\n"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
