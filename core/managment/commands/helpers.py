# Commands
from .help import help
from .gen import gen

commands = {
    '-h': help,
    '--help': help,
    'gen': gen,
}
