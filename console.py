#!/usr/bin/python3
"""
HBNB Console Module
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, s):
        """function on quit
        """
        return True

    def do_EOF(self, s):
        """function on EOF
        """
        print()
        return True

    def help_quit(self):
        """Help when quit is entered
        """
        print("Quit command to exit the program\n")

    def emptyline(self):
        """Do nothing when the user enters an empty line
        """
        pass

    def help_EOF(self):
        """Help when EOF is entered
        """
        print("EOF command to exit the program\n")

    def do_test(self, s):
        """testing the console
        """
        print("Testing!!!!")

    def do_create(self, s):
        """Creates a new instance of BaseModel
        saves it (to the JSON file)
        and prints the id
        """
        args = shlex.split(s)
        if not args or not args[0] or args[0] == "":
            print("** class name missing **")
            return
        class_name = args[0]
        from models.models_dict import all_models
        if class_name not in all_models.keys():
            print("** class doesn't exist **")
            return
        instance = all_models[class_name]()
        instance.save()
        print(f"{instance.id}")

    def help_create(self):
        """shows what create does
        """
        print("creates a new instance of a class")
        print("Usage: create <model_name>\n")

    def do_show(self, s):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = shlex.split(s)
        if not args or not args[0] or args[0] == "":
            print("** class name missing **")
            return
        class_name = args[0]
        from models.base_model import storage
        from models.models_dict import all_models
        if class_name not in all_models.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2 or not args[1]:
            print("** instance id missing **")
            return
        id = args[1]
        all_objects = storage.all()
        key = f"{class_name}.{id}"
        if key not in all_objects.keys():
            print("** no instance found **")
            return
        instance = all_objects[key]
        print(f"{instance}")

    def help_show(self):
        """shows what show does
        """
        print(
            "Prints the string representation of an instance" +
            " based on the class name and id")
        print("Usage: show <model_name> <id>\n")

    def do_all(self, s):
        """Prints all string representation of all instances
        based or not on the class name
        """
        args = shlex.split(s)
        all_objects = storage.all()
        if not args or not args[0] or args[0] == "":
            print(self.list_to_string(all_objects.values()))
            return
        class_name = args[0]
        from models.models_dict import all_models
        if class_name not in all_models.keys():
            print("** class doesn't exist **")
            return
        class_objects = dict(
            filter(lambda item: item[0].startswith(class_name),
                   all_objects.items()))
        my_list = self.list_to_string(class_objects.values())
        if len(my_list) != 0:
            print(my_list)
        else:
            return

    def list_to_string(self, values):
        """converts objects to str representation
        """
        return list(map(lambda obj: str(obj), values))

    def help_all(self):
        """shows what all does
        """
        print("Prints all string representation of all instances" +
              " based or not on the class name")
        print("Usage: all [model_name]\n")

    def do_destroy(self, s):
        """Deletes an instance based on the class name and id
        """
        args = shlex.split(s)
        if not args or not args[0]:
            print("** class name missing **")
            return
        class_name = args[0]
        from models.base_model import storage
        from models.models_dict import all_models
        if class_name not in all_models.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2 or not args[1]:
            print("** instance id missing **")
            return
        id = args[1]
        all_objects = storage.all()
        key = f"{class_name}.{id}"
        if key not in all_objects.keys():
            print("** no instance found **")
            return
        del all_objects[key]
        storage.save()

    def help_destroy(self):
        """shows what destroy does
        """
        print("Deletes an instance based on the class name and id")
        print("Usage: destroy <model_name> <id>\n")

    def do_update(self, s):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = shlex.split(s)
        if not args or not args[0]:
            print("** class name missing **")
            return
        class_name = args[0]
        from models.base_model import storage
        from models.models_dict import all_models
        if class_name not in all_models.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2 or not args[1]:
            print("** instance id missing **")
            return
        id = args[1]
        all_objects = storage.all()
        key = f"{class_name}.{id}"
        if key not in all_objects.keys():
            print("** no instance found **")
            return
        if len(args) < 3 or not args[2]:
            print("** attribute name missing **")
            return
        attrib = args[2]
        if len(args) < 4 or not args[3]:
            print("** value missing **")
            return
        value = args[3]
        if value[0] == '"':
            value = value[1:-1]
        if is_int(value):
            casted_arg = int(value)
        elif is_float(value):
            casted_arg = float(value)
        else:
            casted_arg = str(value)
        setattr(all_objects[key], args[2], casted_arg)
        storage.save()

    def help_update(self):
        """shows what update does
        """
        print("Updates an instance based on the class name and id" +
              " by adding or updating attribute")
        print('update <class name> <id> <attribute name>' +
              '"<attribute value>"\n')

    def do_count(self, arg):
        """count number of objects
        """
        from models.base_model import storage
        from models.models_dict import all_models
        count = 0
        if arg not in all_models.keys():
            print("** class doesn't exist **")
            return
        else:
            all_objects = storage.all()
            check_seq = f"{arg}.*"
            for key in all_objects.keys():
                search_class = re.search(check_seq, key)
                if search_class:
                    count += 1
            print(count)

    def run_command(self, command_name, class_name, args_str):
        """run the command with class name and args
        """
        method_name = f"do_{command_name}"
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            args = class_name
            if args_str != "":
                args = f"{class_name} {args_str}"
            method(args)

    def default(self, arg):
        """if command not in commands"""
        line = arg.split('.')
        if len(line) == 2:
            class_name, command = line
            # if the command taking no args
            if command[-2:] == "()":
                command = command[0:-2]
                args = None
                command_name = command
                args_str = ""
            else:
                # if command taking args
                args = command.split("(")
                command_name = args[0]
                args_str = ""
                args = args[1].split(',')
                id = args[0]
                id = id.replace("\"", "")
                for i in args:
                    i = i.replace(")", "")
                    args_str = f"{args_str} {i}"
            # if the arg is dictionary
            match = re.search(r'\{(.+?)\}', args_str)
            if match:
                arg_str = None
                content = match.group(1)
                rm = ["\"", "\'", ":"]
                for c in rm:
                    content = content.replace(c, "")
                content = content.split('  ')
                for i in content:
                    args_str = f"{id} {i}"
                    self.run_command(command_name, class_name, args_str)
                args_str = None
            if args_str is not None:
                self.run_command(command_name, class_name, args_str)


def is_int(value):
    """check if int"""
    try:
        int_value = int(value)
        return True
    except ValueError:
        return False


def is_float(value):
    """check if number is float
    """
    try:
        float_value = float(value)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
