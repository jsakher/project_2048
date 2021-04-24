""" Data and plots generator """

import numpy as np
from game import Main
import matplotlib.pyplot as plt
import seaborn as sns
import time

def Make_stats(nb_game=1000):
    """
    Plays several games with random and clockwise strategies.  
    Calculates empirical mean and standard deviation with your data and
    compare them with the original data. (300 000 game played)  

    Display the result with as kernel density estimate (KDE) plot that shows
    the distribution of score and an histogram with max cell get.

    :param int nb_game: Amount of game played by IA, default = 1000 
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

    print(f'Empirical mean of random strategy score you computed is {round(Mean_random)}')
    print(f'Empirical mean of this strategy score with 300 000 tries is 1095')
    print(f'Empirical mean of clockwise strategy score you computed is {round(Mean_clock)}')
    print(f'Empirical mean of this strategy score with 300 000 tries is 2310')
    print(f'-------------------------------------------------------- \n')

    Var_random = 1/nb_game * sum((score_random - Mean_random)**2)
    Var_clockwise = 1/nb_game * sum((score_clock - Mean_clock)**2)

    std_random = np.sqrt(Var_random)
    std_clock = np.sqrt(Var_clockwise)

    print(f'Standard deviation of random strategy score of the games you computed is {round(std_random)} ')
    print(f'Standard deviation of random strategy with 300 000 tries is 534')
    print(f'Standard deviation of clockwise strategy score of the games you computed is {round(std_clock)} ')
    print(f'Standard deviation of clockwise strategy score with 300 000 tries is 1082')

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
    #plt.show()

    plt.plot()
    plt.subplot(2, 1, 1)
    plt.hist(maxcell_random, label='Random strategy',
             bins=20, color=random_color)
    plt.legend(loc='upper right')
    plt.title("Distribution of max score")

    plt.subplot(2, 1, 2)
    plt.hist(maxcell_clock, label='Clockwise strategie',
             bins=20, color=clockwise_color)
    plt.legend(loc='upper right')
    plt.xlabel("Max cell")
    plt.savefig('AI_maxcell_random_clockwise.svg')
    #plt.show()

# Execution of Make_stats function with a specific number of games launched
def time_MS(n):
    start =time.time()
    Make_stats(n)
    end= time.time()
    return (print("Temps passé pour exécuter la commande: {0:.5f} s.".format(end - start)))
time_MS(250)





# def tgm(strat1):
#     A = Main.Game_2048()
#     A = getattr(A, f"{strat1}")()

# A = Main.Game_2048()

# getattr(A, "main")()