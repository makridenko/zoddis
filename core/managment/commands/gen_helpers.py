# Global modules
import sys
import shutil
import fileinput

# Zoddis modules
from . import templates


HELP_GEN_COMMAND = 'usage: zds gen -t <name> -b <port> -f <port>'

GEN_KEYS = {
    '-t': ['', str],
    '-b': [0, int],
    '-f': [0, int],
}


def valid_keys():
    if GEN_KEYS['-t'][0] == '': return False
    if GEN_KEYS['-b'][0] == 0: return False
    if GEN_KEYS['-f'][0] == 0: return False
    return True


def gen_dirs(project_dir):
    dirs = [
        '%s',
        '%s/frontend/workdir',
        '%s/frontend/docker/nodejs',
        '%s/backend/workdir',
        '%s/backend/docker/django',
        '%s/volumes/data',
    ]

    for i in range(len(dirs)):
        dirs[i] = dirs[i] % (project_dir)

    return dirs


# Function for copy file from template
def copy_file(name, dest_path):
    template_path = templates.__path__[0] + '/' + name
    shutil.copy2(template_path, dest_path)


# Function for replace str line
def replace_str(file_path, search_exp, replace_exp):
    for line in fileinput.input(file_path, inplace=1):
        if search_exp in line:
            line = line.replace(search_exp, replace_exp)
        sys.stdout.write(line)
