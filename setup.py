from setuptools import setup, find_packages
from Game2048 import __version__ as current_version
setup(name='Game2048',
      version=current_version,
      packages=find_packages(
          include=['Game2048', 'Game2048.functions', 'Game2048.game', 'Game2048.visual_game']),
      description='The 2048 game and a few statistics results on it',
      url='https://github.com/Nathanesteve/project_2048',
      author='Nathan Esteve ; Jalal Sakher ; Ayoub Aarab ; Elucson Jean-Baptiste',
      author_email='',
      license='MIT',)
