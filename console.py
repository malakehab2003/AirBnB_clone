#!/usr/bin/python3
"""console of airbnb
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """the command line of airbnb
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """handle non-interactive mood
        """
        print()
        return True

    def emptyline(self):
        """when pressed enter and no command
        """
        pass

    def do_create(self, arg):
        """create new instanse
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            # the first place
            create_instanse = class_dict[arg]()
            create_instanse.save()
            print(create_instanse.id)

    def do_show(self, arg):
        """show the string representation of an instance
        """
        class_id = handle_error(arg)
        if class_id:
            all_objs = storage.all()
            print(all_objs[class_id])

    def do_destroy(self, arg):
        """destroy instanse of the json file
        """
        class_id = handle_error(arg)
        if class_id:
            all_objs = storage.all()
            del all_objs[class_id]
            storage.save()

    def do_all(self, arg):
        """print all the instanses of class
        """
        all_objs = storage.all()
        list_objs = []
        for value in all_objs.values():
            list_objs.append(str(value))
        if len(arg) == 0:
            print(list_objs)
        else:
            # the second place
            if arg not in class_dict.keys():
                print("** class doesn't exist **")
            else:
                print(list_objs)

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


class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
