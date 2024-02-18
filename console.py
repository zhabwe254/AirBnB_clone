# console.py

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON file, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in globals():
                raise NameError
            if len(args) < 2:
                print("** instance id missing **")
                return
            objs = storage.all()
            key = args[0] + "." + args[1]
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in globals():
                raise NameError
            if len(args) < 2:
                print("** instance id missing **")
                return
            objs = storage.all()
            key = args[0] + "." + args[1]
            if key in objs:
                objs.pop(key)
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representations of all instances based or not on class name."""
        args = arg.split()
        objs = storage.all()
        if not arg:
            print([str(objs[obj]) for obj in objs])
            return
        try:
            if args[0] not in globals():
                raise NameError
            print([str(objs[obj]) for obj in objs if args[0] in obj])
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on class name and id by adding or updating attribute."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in globals():
                raise NameError
            if len(args) < 2:
                print("** instance id missing **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            objs = storage.all()
            key = args[0] + "." + args[1]
            if key in objs:
                obj = objs[key]
                setattr(obj, args[2], args[3])
                obj.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

