__version__ = '0.0.1'

from Game2048.game.Main import Game_2048, Game_6561
from Game2048.visual_game import visual_game
from Game2048.ai_versus import versus


def launch_2048():
    Game = Game_2048()
    Game.main()


def launch_2048_demo():
    AI_one = Game_2048()
    AI_one.demo()


def launch_6561():
    Game = Game_6561()
    Game.main()


def launch_2048_visual():
    visual_game()
