from setuptools import setup
from setuptools import find_packages


setup(name='zoddis',
      version='0.0.1',
      author='Alex Makridenko',
      author_email='makridenko.a@yandex.ru',
      scripts=['bin/zoddis.py'],
      entry_points={'console_scripts': [
          'zds = core.managment: execute_from_command_line'
      ]},
      install_requires=[
      ],
      include_package_data=True,
      packages=find_packages()
)
