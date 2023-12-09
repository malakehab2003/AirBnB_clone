#!/usr/bin/python3
"""
HBNB Console Module
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


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
        print(self.list_to_string(class_objects.values()))

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

    def help_destroy(self):
        """shows what destroy does
        """
        print("Deletes an instance based on the class name and id")
        print("Usage: destroy <model_name> <id>\n")

    def do_update(self, arg):
        """update data of an instanse
        """
        class_id = handle_error(arg)
        arg_list = arg.split()
        all_objs = storage.all()
        if len(arg_list) < 3:
            print("** attribute name missing **")
        elif len(arg_list) < 4:
            print("** value missing **")
        else:
            if arg_list[3][1:-1].isdigit():
                casted_arg = int(arg_list[3][1:-1])
            elif is_float(arg_list[3][1:-1]):
                casted_arg = float(arg_list[3][1:-1])
            else:
                casted_arg = str(arg_list[3][1:-1])
            setattr(all_objs[class_id], arg_list[2], casted_arg)
            storage.save()

    def help_update(self):
        """shows what update does
        """
        print("Updates an instance based on the class name and id" +
              " by adding or updating attribute")
        print('update <class name> <id> <attribute name>' +
              '"<attribute value>"\n')

class_dict = {
        "BaseModel": BaseModel
    }

def handle_error(arg):
    """handle some errors
    """
    arg_list = arg.split()

    if len(arg_list) == 0 or arg_list is None:
        print("** class name missing **")
    # third and final place
    elif arg_list[0] not in class_dict.keys():
        print("** class doesn't exist **")
    elif len(arg_list) < 2:
        print("** instance id missing **")
    else:
        class_id = "{}.{}".format(arg_list[0], arg_list[1])
        all_objs = storage.all()
        if class_id in all_objs:
            return class_id
        else:
            print("** no instance found **")
            return None

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
