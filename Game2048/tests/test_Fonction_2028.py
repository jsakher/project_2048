from Game2048 import Fonction_2048
import unittest
import random
random.seed(1234)
class TestFonction(unittest.TestCase):
    def setUp(self):
        self.grid_new = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.grid_2048 = [[256, 4096, 16, 32], [8, 4, 8, 2], [2, 2, 16, 32], [2048, 64, 64, 2]]
        self.grid_np = [[8, 4, 8, 4],[2, 8, 4, 8],[4, 2, 8, 4],[2, 4, 2, 8]]
        self.score = 2048
    def test_sup2048(self):
        assert Fonction_2048.sup_2048(self.grid_2048) == 2
        assert Fonction_2048.sup_2048(self.grid_new) == 0
    def test_possible_action(self):
        assert Fonction_2048.possible_action(self.grid_np) == False
        assert Fonction_2048.possible_action(self.grid_2048) == True
    def test_stop_game(self):
        assert Fonction_2048.stop_game(self.grid_np) == False
        assert Fonction_2048.stop_game(self.grid_2048) == True
    # def test_state_game(self):
    #     assert Fonction_2048.state_game(self.grid_2048, self.score) == '------------'

#Fonction_2048.state_game([[256, 4096, 16, 32], [8, 4, 8, 2], [2, 2, 16, 32], [2048, 64, 64, 2]], 103)
# print(2048,'\n', 103)