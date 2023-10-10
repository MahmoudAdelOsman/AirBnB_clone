#!/usr/bin/env python3
"""module contain notes about cmd class"""
import cmd
import os
import sys


class HBNBCommand(cmd.Cmd):
    """Simple command processor for AirBnB_c."""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """quit command to exit program\n"""
        print()
        return True

    def do_clear(self, args):
        """clear terminal"""
        os.system("clear")

    def default(self, line: str) -> None:
        print(f"command \"{line}\" not found")

    def emptyline(self):
        """when pressing enter nothing happens"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
