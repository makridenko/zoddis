# Global modules
import sys

# All commands
from .commands.helpers import commands
from .commands.help import help

class ManageUtil:
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]

    def default(self):
        help()

    def execute(self):
        try:
            subcommand = self.argv[1]
            commands.get(subcommand, self.default)()
        except IndexError:
            help()


def execute_from_command_line(argv=None):
    util = ManageUtil(argv)
    util.execute()
