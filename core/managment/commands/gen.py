# Global moduls
import os
import subprocess

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

    copy_file(
        'dckrcmps',
        f'{project_dir}/docker-compose.yml',
    )

    replace_str(
        f'{project_dir}/docker-compose.yml',
        '{front_ports}',
        str(GEN_KEYS['-f'][0]),
    )
    replace_str(
        f'{project_dir}/docker-compose.yml',
        '{back_ports}',
        str(GEN_KEYS['-b'][0]),
    )

    copy_file(
        'global_run',
        f'{project_dir}/run.sh',
    )

    subprocess.call(
        f'cd {project_dir} && chmod +x run.sh',
        shell=True,
    )

    replace_str(
        f'{project_dir}/run.sh',
        '{prj_name}',
        str(GEN_KEYS['-t'][0]),
    )

    copy_file(
        'front_dockerfile',
        f'{project_dir}/frontend/docker/nodejs/Dockerfile',
    )

    copy_file(
        'back_dockerfile',
        f'{project_dir}/backend/docker/django/Dockerfile',
    )

    copy_file(
        'requirements.txt',
        f'{project_dir}/backend/docker/django/requirements.txt',
    )

    copy_file(
        'back_gitignore',
        f'{project_dir}/backend/workdir/.gitignore',
    )

    copy_file(
        'back_run',
        f'{project_dir}/backend/workdir/run.sh',
    )

    subprocess.call(
        f'cd {project_dir}/backend/workdir && chmod +x run.sh',
        shell=True,
    )

    copy_file(
        'front_gitignore',
        f'{project_dir}/frontend/workdir/.gitignore',
    )

    copy_file(
        'front_run',
        f'{project_dir}/frontend/workdir/run.sh'
    )

    subprocess.call(
        f'cd {project_dir}/frontend/workdir && chmod +x run.sh',
        shell=True,
    )

    copy_file(
        'global_gitignore',
        f'{project_dir}/.gitignore',
    )

    subprocess.call(
        f'cd {project_dir}/backend/workdir && django-admin startproject app',
        shell=True,
    )

    subprocess.call(
        f'cd {project_dir}/backend/workdir && mv app/ app_/ && mv app_/* . && rm -rf app_/',
        shell=True,
    )

    subprocess.call(
        f'cd {project_dir}/frontend/workdir && create-react-app app && mv app/* . && rm -rf app/',
        shell=True,
    )
