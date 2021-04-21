import numpy as np
import Main
import matplotlib.pyplot as plt
import seaborn as sns


def Make_stats(nb_game=1000):
    """
    Play several number of game played with random and clockwise strategies.  
    Calculates empirical mean and standard deviation with your data,
    compare them with our data. (300 000 game played)  

    Display the result with à kekplot that show you the distrubution of score
    and an histogram with max cell get.  

    :param nb_game: Number of game play by IA, default = 1000  
    :type nb_game: int  
    """

    score_random = []
    score_clock = []
    maxcell_random = []
    maxcell_clock = []
    print('processing......')
    print('that must take time.....')

    # Compute nb_game game and store the result

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

    print(f'Empicial mean for random strategy that you compute is {round(Mean_random)}')
    print(f'Empicial mean with this strategy and with 300 000 try is 1095')
    print(f'Empicial mean for clockwise strategy that you compute is {round(Mean_clock)}')
    print(f'Empicial mean with this strategy and with 300 000 try is 2310')
    print(f'-------------------------------------------------------- \n')

    Var_random = 1/nb_game * sum((score_random - Mean_random)**2)
    Var_clockwise = 1/nb_game * sum((score_clock - Mean_clock)**2)

    std_random = np.sqrt(Var_random)
    std_clock = np.sqrt(Var_clockwise)

    print(f'The standard deviation of random strategy that you compute is {round(std_random)} ')
    print(f'The standard deviation of random strategy with 300 000 try is 534')
    print(f'The standard deviation of clockwise strategy that you compute is {round(std_clock)} ')
    print(f'The standard deviation of clockwise strategy  with 300 000 try is 1082')

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
    plt.title("Distribution of max score")

    plt.subplot(2, 1, 2)
    plt.hist(maxcell_clock, label='Clockwise strategie',
             bins=20, color=clockwise_color)
    plt.legend(loc='upper right')
    plt.xlabel("Max cell")
    plt.savefig('AI_maxcell_random_clockwise.svg')
    plt.show()

