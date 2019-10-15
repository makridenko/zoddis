# Global moduls
import os

from .gen_helpers import *


def gen():
    keys = sys.argv[1:]

    for i, key in enumerate(keys):
        if key in GEN_KEYS:
            try:
                GEN_KEYS[key][0] = GEN_KEYS[key][1](keys[i+1])
            except:
                print(HELP_GEN_COMMAND)
                return False

    if not valid_keys():
        print(HELP_GEN_COMMAND)
        return False

    dirs = []

    # project directory
    project_dir = GEN_KEYS['-t'][0]

    if os.path.isdir(GEN_KEYS['-t'][0]):
        print('folder %s already exists' % (GEN_KEYS['-t'][0]))
        return False

    for dir in gen_dirs(project_dir):
        os.makedirs(dir)
