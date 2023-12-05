#!/usr/bin/python3
"""
HBNB Console Module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    the entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, s):
        """
        function on quit
        """
        return True

    def do_EOF(self, s):
        """
        function on EOF
        """
        return True

    def help_quit(self):
        """
        Help when quit is entered
        """
        print("Quit command to exit the program")

    def emptyline(self):
        """Do nothing when the user enters an empty line"""
        pass

    def help_EOF(self):
        """
        Help when EOF is entered
        """
        print("EOF command to exit the program")

    def do_test(self, s):
        """
        testing the console
        """
        print("Testing!!!!")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
