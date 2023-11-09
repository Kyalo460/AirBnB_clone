#!/usr/bin/env python3
"""Console.

Contains the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class.

    This is the command interpreter class.
    """

    prompt = "(hbnb) "

    def cmdloop(self):
        """cmdloop."""
        return super().cmdloop()

    def emptyline(self):
        """Empty Line command override.

        This is so that an empty line + ENTER shouldn't execute anything.
        """
        return

    def do_quit(self, line):
        """Quit.
        
        Quit command to exit the program.
        """
        quit(0)

    def do_EOF(self, line):
        """Exit the console."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
