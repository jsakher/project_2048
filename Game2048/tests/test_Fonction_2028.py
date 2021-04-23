from Game2048.functions import Fonction_2048
import unittest
from unittest.mock import patch
import random
# random.seed(123)
# print(random.randint(a=0, b=3))
# print(random.uniform(a=0, b=1))
class TestFonction(unittest.TestCase):
    def setUp(self):
        self.grid_new = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.grid_2048 = [[256, 4096, 16, 32], [8, 4, 8, 2], [2, 2, 16, 32], [2048, 64, 64, 2]]
        self.grid_np = [[8, 4, 8, 4],[2, 8, 4, 8],[4, 2, 8, 4],[2, 4, 2, 8]]
        self.score = 2048
        self.grid = [[0, 2, 2, 0],[2, 0, 0, 2],[0, 2, 0, 4],[8, 8, 0, 8]]
    
    def test_sup2048(self):
        assert Fonction_2048.sup_2048(self.grid_2048) == 2
        assert Fonction_2048.sup_2048(self.grid_new) == 0
    def test_possible_action(self):
        assert Fonction_2048.possible_action(self.grid_np) == False
        assert Fonction_2048.possible_action(self.grid_2048) == True
    def test_stop_game(self):
        assert Fonction_2048.stop_game(self.grid_np) == False
        assert Fonction_2048.stop_game(self.grid_2048) == True
    @patch('builtins.print')
    def test_state_game(self, mock_print):
         Fonction_2048.state_game(self.grid_2048, self.score)
         mock_print.assert_called_with(self.grid_2048[0], '\n', self.grid_2048[1], '\n', self.grid_2048[2], '\n', self.grid_2048[3], '\n', f'Your score is {self.score}')
        #  mock_print.assert_called_with(self.grid_2048[1])
        #  mock_print.assert_called_with(self.grid_2048[2])
        #  mock_print.assert_called_with(self.grid_2048[3])
        #  mock_print.assert_called_with(f"Your score is {self.score}")
    # def test_newcell_start(self):
    #     random.seed(123) #makes uniform in [0,1] < 0.9, random.seed(1234) makes it otherwise.
    #     assert Fonction_2048.new_game(self.grid_new) == ([[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] or [[0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] or [[0, 0, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] or [[0, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] or [[0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]or [[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] or [[0, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0]] or [[0, 0, 0, 0], [0, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0]]or [[0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0]] or [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0]] or [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 0]]or [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2], [0, 0, 0, 0]] or [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0]] or [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0]]or [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0]] or [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]])
    def test_stack(self):
        assert Fonction_2048.stack(self.grid) == [[2, 2, 0, 0], [2, 2, 0, 0], [2, 4, 0, 0], [8, 8, 8, 0]]
    def test_merge_left(self):
        assert Fonction_2048.merge_left(self.grid, self.score) == ([[0, 4, 0, 0], [2, 0, 0, 2], [0, 2, 0, 4], [16, 0, 0, 8]], 2068)
    def test_transpose(self):
        assert Fonction_2048.transpose(self.grid) == [[0, 2, 0, 8], [2, 0, 2, 8], [2, 0, 0, 0], [0, 2, 4, 8]]
    def test_inverse(self):
        assert Fonction_2048.inverse(self.grid) == [[0, 2, 2, 0], [2, 0, 0, 2], [4, 0, 2, 0], [8, 0, 8, 8]]
    def test_rotation(self):
        assert Fonction_2048.rotation(self.grid_2048) == [[32, 16, 4096, 256], [2, 8, 4, 8], [32, 16, 2, 2], [2, 64, 64, 2048]]
    def test_left_movement(self):
        assert Fonction_2048.left_movement(self.grid, self.score) == ([[4, 0, 0, 0], [4, 0, 0, 0], [2, 4, 0, 0], [16, 8, 0, 0]], 2072)    
    def test_up_movement(self):
        assert Fonction_2048.up_movement(self.grid, self.score) == ([[2, 4, 2, 2], [8, 8, 0, 4], [0, 0, 0, 8], [0, 0, 0, 0]], 2052)
    def test_down_movement(self):
        assert Fonction_2048.down_movement(self.grid, self.score) == ([[0, 0, 0, 0], [0, 0, 0, 2], [2, 4, 0, 4], [8, 8, 2, 8]], 2052)
    def test_right_movement(self):
        assert Fonction_2048.right_movement(self.grid, self.score) == ([[0, 0, 0, 4], [0, 0, 0, 4], [0, 0, 2, 4], [0, 0, 8, 16]], 2072)
