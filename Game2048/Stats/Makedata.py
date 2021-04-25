import numpy as np
import Game2048.game.Main as Main


def makedata(nb_data):
    """
    This function generate a data set : mean and max cell
    over nb_data games with all of 4 strategies.
    The data are store in Your_result directory

    :param nb_data: number of game that you want to analyse
    :type nb_data: integer

    """

    score_random = []
    score_clock = []
    score_opp = []
    score_adj = []

    maxcell_random = []
    maxcell_clock = []
    maxcell_opp = []
    maxcell_adj = []

    for i in range(nb_data):

        AI_one = Main.Game_2048()
        AI_one.random_2048()
        AI_one.maxcell_find()
        maxcell_random.append(AI_one.maxcell)
        score_random.append(AI_one.score)

        AI_two = Main.Game_2048()
        AI_two.clockwise_2048()
        AI_two.maxcell_find()
        maxcell_clock.append(AI_two.maxcell)
        score_clock.append(AI_two.score)

        AI_three = Main.Game_2048()
        AI_three.opposite_2048()
        AI_three.maxcell_find()
        maxcell_opp.append(AI_three.maxcell)
        score_opp.append(AI_three.score)

        AI_four = Main.Game_2048()
        AI_four.adjacent_2048()
        AI_four.maxcell_find()
        maxcell_adj.append(AI_four.maxcell)
        score_adj.append(AI_four.score)

    data_random = np.asarray(score_random)
    data_clock = np.array(score_clock)
    data_opp = np.asarray(score_opp)
    data_adj = np.array(score_adj)

    np.savetxt('Game2048/Stats/Your_result/Score_random.txt', data_random)
    np.savetxt('Game2048/Stats/Your_result/Score_clockwise.txt', data_clock)
    np.savetxt('Game2048/Stats/Your_result/Score_opposite.txt', data_opp)
    np.savetxt('Game2048/Stats/Your_result/Score_adjacent.txt', data_adj)

    np.savetxt('Game2048/Stats/Your_result/AI_maxcell_random.txt',
               maxcell_random)
    np.savetxt('Game2048/Stats/Your_result/AI_maxcell_clockwise.txt',
               maxcell_clock)
    np.savetxt('Game2048/Stats/Your_result/AI_maxcell_opposite.txt',
               maxcell_opp)
    np.savetxt('Game2048/Stats/Your_result/AI_maxcell_adjacent.txt',
               maxcell_adj)

makedata(10)