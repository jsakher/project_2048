""" Data and plots generator """

import numpy as np
from Game2048.Stats import Main
import matplotlib.pyplot as plt
import seaborn as sns
import time


def statsmaker1(nb_game=1000):
    """
    Plays several games with random and clockwise strategies.
    Calculate empirical mean and standard deviation with your data and
    compare them with the original data. (300 000 games played)

    Display the result with as kernel density estimate (KDE) plot that shows
    the distribution of score and an histogram with max cell gets.

    :param nb_game: Amount of game played by IA, default = 1000
    :type nb_game: int
    """

    score_random = []
    score_clock = []
    maxcell_random = []
    maxcell_clock = []
    print('processing......')
    print('that must take time.....')

    # Compute nb_game games and store the result

    for i in range(nb_game):

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

    score_random = np.asarray(score_random)
    score_clock = np.asarray(score_clock)
    Mean_random = np.mean(score_random)
    Mean_clock = np.mean(score_clock)

    # Display your result and compare them to "real" value

    print(f'Empirical mean of random strategy score you computed is {Mean_random}')
    print('Empirical mean of this strategy score with 300 000 tries is 1094,66')
    print(f'Empirical mean of clockwise strategy score you computed is {Mean_clock}')
    print('Empirical mean of this strategy score with 300 000 tries is 2309,67')
    print('-------------------------------------------------------- \n')

    Var_random = 1/nb_game * sum((score_random - Mean_random)**2)
    Var_clockwise = 1/nb_game * sum((score_clock - Mean_clock)**2)

    std_random = np.sqrt(Var_random)
    std_clock = np.sqrt(Var_clockwise)

    print(f'Standard deviation of random strategy score of the games you computed is {std_random} ')
    print('Standard deviation of random strategy with 300 000 tries is 533,89')
    print(f'Standard deviation of clockwise strategy score of the games you computed is {std_clock} ')
    print('Standard deviation of clockwise strategy score with 300 000 tries is 1081,97')

    random_color = '#8A2BE2'
    clockwise_color = '#FF8C00'
    plt.figure()
    sns.kdeplot(score_random, bw_adjust=0.3, legend=True,
                color=random_color)
    sns.kdeplot(score_clock, bw_adjust=0.3,
                legend=True, color=clockwise_color)
    plt.legend(labels=['Random strategy', 'Clockwise strategy'])
    plt.title("Distribution of score with random and clockwise strategies")
    plt.xlabel("score")
    plt.show()

    plt.plot()
    plt.subplot(2, 1, 1)
    plt.hist(maxcell_random, label='Random strategy',
             bins=20, color=random_color)
    plt.legend(loc='upper right')
    plt.ylabel("Number of appearance")
    plt.xlim(0, 1024)
    plt.title("Distribution of max score")

    plt.subplot(2, 1, 2)
    plt.hist(maxcell_clock, label='Clockwise strategy',
             bins=20, color=clockwise_color)
    plt.legend(loc='upper right')
    plt.xlabel("Max cell")
    plt.ylabel("Number of appearance")
    plt.xlim(0, 1024)
    # plt.savefig('AI_maxcell_random_clockwise.svg')
    plt.show()


def statsmaker2(nb_game=1000):
    """
    Plays several games with adjacent and opposite strategies.
    Calculate empirical mean and standard deviation with your data and
    compare them with the original data. (300 000 games played)

    Display the result with as kernel density estimate (KDE) plot that shows
    the distribution of score and an histogram with max cell gets.

    :param nb_game: Amount of game played by IA, default = 1000
    :type nb_game: int
    """

    score_opp = []
    score_adj = []
    maxcell_opp = []
    maxcell_adj = []
    print('processing......')
    print('that must take time.....')

    # Compute nb_game games and store the result

    for i in range(nb_game):

        AI_one = Main.Game_2048()
        AI_one.opposite_2048()
        AI_one.maxcell_find()
        maxcell_opp.append(AI_one.maxcell)
        score_opp.append(AI_one.score)

        AI_two = Main.Game_2048()
        AI_two.adjacent_2048()
        AI_two.maxcell_find()
        maxcell_adj.append(AI_two.maxcell)
        score_adj.append(AI_two.score)

    score_opp = np.asarray(score_opp)
    score_adj = np.asarray(score_adj)
    Mean_opp = np.mean(score_opp)
    Mean_adj = np.mean(score_adj)

    # Display your result and compare them to "real" value

    print(f'Empirical mean of opposite strategy score you computed is {Mean_opp}')
    print('Empirical mean of this strategy score with 300 000 tries is 88,01')
    print(f'Empirical mean of adjacent strategy score you computed is {Mean_adj}')
    print('Empirical mean of this strategy score with 300 000 tries is 120,45')
    print('-------------------------------------------------------- \n')

    Var_opp = 1/nb_game * sum((score_opp - Mean_opp)**2)
    Var_adj = 1/nb_game * sum((score_adj - Mean_adj)**2)

    std_opp = np.sqrt(Var_opp)
    std_adj = np.sqrt(Var_adj)

    print(f'Standard deviation of opposite strategy score of the games you computed is {std_opp} ')
    print('Standard deviation of opposite strategy with 300 000 tries is 25,25')
    print(f'Standard deviation of adjacent strategy score of the games you computed is {std_adj} ')
    print('Standard deviation of adjacent strategy score with 300 000 tries is 104,75')

    opposite_color = '#1E90FF'
    adjacent_color = '#6e3300'
    plt.figure()
    sns.kdeplot(score_opp, bw_adjust=0.3, legend=True,
                color=opposite_color)
    sns.kdeplot(score_adj, bw_adjust=0.3,
                legend=True, color=adjacent_color)
    plt.legend(labels=['Opposite strategy', 'Adjacent strategy'])
    plt.title("Distribution of score with opposite and random strategies")
    plt.xlabel("score")
    plt.show()

    plt.plot()
    plt.subplot(2, 1, 1)
    plt.hist(maxcell_opp, label='Opposite strategy',
             bins=20, color=opposite_color)
    plt.legend(loc='upper right')
    plt.ylabel("Number of appearance")
    plt.xlim(0, 128)
    plt.title("Distribution of max score")

    plt.subplot(2, 1, 2)
    plt.hist(maxcell_adj, label='Adjacent strategy',
             bins=20, color=adjacent_color)
    plt.legend(loc='upper right')
    plt.xlabel("Max cell")
    plt.xlim(0, 128)
    plt.ylabel("Number of appearance")
    # plt.savefig('AI_maxcell_opposite_adjacent.svg')
    plt.show()


# Execution of statsmaker1 function with a specific number of games launched


statsmaker1()
statsmaker2()
