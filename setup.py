from setuptools import setup, find_namespace_packages

setup(name='hmcli',
      packages=find_namespace_packages(include='hmcli.*'),
      entry_points={
          'console_scripts': [
              'hmcli=hmcli.__main__:main'
          ]
      })
