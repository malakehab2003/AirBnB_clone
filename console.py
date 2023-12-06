#!/usr/bin/python3
"""
HBNB Console Module
"""
import cmd
import shlex


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

    def do_create(self, s):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file)
        and prints the id
        """
        args = shlex.split(s)
        if not args or not args[0]:
            print("** class name missing **")
            return
        class_name = args[0]
        from models.base_model import BaseModel
        classes = {"BaseModel": BaseModel}
        if class_name not in classes.keys():
            print("** class doesn't exist **")
            return
        instance = classes[class_name]()
        instance.save()
        print(f"{instance.id}")

    def help_create(self):
        """
        shows what create does
        """
        print("creates a new instance of a class")
        print("Usage: create <model_name>")

    def do_show(self, s):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = shlex.split(s)
        if not args or not args[0]:
            print("** class name missing **")
            return
        class_name = args[0]
        from models.base_model import storage
        classes = ["BaseModel"]
        if class_name not in classes:
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
        """
        shows what show does
        """
        print(
            "Prints the string representation of an instance" +
            " based on the class name and id")
        print("Usage: show <model_name> <id>")

    def do_all(self, s):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        from models.base_model import storage
        args = shlex.split(s)
        all_objects = storage.all()
        if not args or not args[0]:
            print(self.list_to_string(all_objects.values()))
            return
        class_name = args[0]
        classes = ["BaseModel"]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        class_objects = dict(
            filter(lambda item: item[0].startswith(class_name),
                   all_objects.items()))
        print(self.list_to_string(class_objects.values()))

    def list_to_string(self, values):
        """
        converts objects to str representation
        """
        return list(map(lambda obj: str(obj), values))

    def help_all(self):
        """
        shows what all does
        """
        print("Prints all string representation of all instances" +
              " based or not on the class name")
        print("Usage: all [model_name]")

    def do_destroy(self, s):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(s)
        if not args or not args[0]:
            print("** class name missing **")
            return
        class_name = args[0]
        from models.base_model import storage
        classes = ["BaseModel"]
        if class_name not in classes:
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
        storage.delete_object(key)

    def help_destroy(self):
        """
        shows what destroy does
        """
        print("Deletes an instance based on the class name and id")
        print("Usage: destroy <model_name> <id>")

    def do_update(self, s):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = shlex.split(s)
        if not args or not args[0]:
            print("** class name missing **")
            return
        class_name = args[0]
        from models.base_model import storage
        classes = ["BaseModel"]
        if class_name not in classes:
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
        storage.update_object(key, attrib, value)

    def help_update(self):
        """
        shows what update does
        """
        print("Updates an instance based on the class name and id" +
              " by adding or updating attribute")
        print('update <class name> <id> <attribute name> "<attribute value>"')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
