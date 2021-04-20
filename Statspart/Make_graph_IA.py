import random
import numpy as np
from Game2048.Main import Game_2048
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

just_plot = True


# DON'T RUN 

if just_plot is False:

    stockage_score_random = []
    stockage_score_clockwise = []
    stockage_maxcell_random = []
    stockage_maxcell_clockwise = []
    for i in range(300000):
        AI_one = Game_2048()
        AI_one.random_2048()
        AI_one.maxcell_find()
        stockage_maxcell_random.append(AI_one.maxcell)
        stockage_score_random.append(AI_one.score)

        AI_two = Game_2048()
        AI_two.clockwise_2048()
        AI_two.maxcell_find()
        stockage_maxcell_clockwise.append(AI_two.maxcell)
        stockage_score_clockwise.append(AI_two.score)
        print(i)


    data_random = np.array(stockage_score_random)
    data_clockwise = np.array(stockage_score_clockwise)

<<<<<<< HEAD
    np.savetxt('Storage_AI_score_random.txt', data_random)
    np.savetxt('Storage_AI_score_clockwise.txt', data_clockwise)
    np.savetxt('Storage_AI_maxcell_random.txt', stockage_maxcell_random)
    np.savetxt('Storage_AI_maxcell_clockwise.txt',  stockage_maxcell_clockwise)
=======
    np.savetxt('Storage_AI_score_opposite.txt', data_opposite)
    np.savetxt('Storage_AI_score_adjacent.txt', data_adjacent)
    np.savetxt('Storage_AI_maxcell_opposite.txt', stockage_maxcell_opposite)
    np.savetxt('Storage_AI_maxcell_adjacent.txt', stockage_maxcell_adjacent)
>>>>>>> 8642bd84dcae0b38f1b3fc143e47d33d5368c7e0



else:


    random_color = '#8A2BE2'
    clockwise_color = '#FF8C00'
    data_score_random = np.loadtxt('Storage_AI_score_random.txt')
    data_score_clockwise = np.loadtxt('Storage_AI_score_clockwise.txt')

    Mean_storage_random = (1/np.arange(1, len(data_score_random) + 1)) * np.cumsum(data_score_random)
    Mean_storage_clockwise = (1/np.arange(1, len(data_score_clockwise) + 1)) * np.cumsum(data_score_clockwise)



    empirical_mean_random = Mean_storage_random[len(Mean_storage_random) - 1]
    empirical_mean_clockwise = Mean_storage_clockwise[len(Mean_storage_clockwise) - 1]

    print(f'Empirical mean for random strategie is {empirical_mean_random}')
    print(f'Empirical mean for random clockwise is {empirical_mean_clockwise}')

    plt.figure()
    plt.plot(Mean_storage_random, color=random_color, label='random movement')
    plt.plot(Mean_storage_clockwise, color=clockwise_color, label='clockwise movement')
    plt.title("Empirical mean convergence")
    plt.legend()
    plt.xlabel("Number of data")
    plt.ylabel("Empirical mean")
    plt.xlim(0, 1500)
<<<<<<< HEAD
    plt.ylim(0,4000)
    plt.savefig('AI_score_randomvsclockwise.pdf')
    plt.show()


    d = {'random strategy': data_score_random, 'clockwise strategy': data_score_clockwise}
=======
    plt.ylim(0, 4000)
    plt.savefig('AI_score.pdf')
    plt.show()


    d = {'Random strategy': data_score_random, 'Clockwise strategy': data_score_clockwise}
>>>>>>> 8642bd84dcae0b38f1b3fc143e47d33d5368c7e0
    df = pd.DataFrame(d)
    plt.figure()
    sns.kdeplot(data_score_random, bw_adjust=0.1, legend=True, color=random_color)
    sns.kdeplot(data_score_clockwise, bw_adjust=0.1, legend=True, color=clockwise_color)
    # plt.vlines(empirical_mean_random, 0, 0.00125, colors='black')
    # plt.vlines(empirical_mean_clockwise, 0, 0.00125, colors='black')
<<<<<<< HEAD
    plt.legend(labels=['random strategie','clockwise strategie'])
    plt.title("Distribution of score with random et clockwise strategies")
    plt.xlabel("score")
    plt.savefig('AI_distribution_randomvsclockwise.pdf')
=======
    plt.legend(labels=['Random strategy', 'Clockwise strategy'])
    plt.title("Distribution of score with random et clockwise strategies")
    plt.xlabel("Score")
    plt.savefig('AI_distribution.pdf')
>>>>>>> 8642bd84dcae0b38f1b3fc143e47d33d5368c7e0


    plt.show()


    data_maxcell_random = np.loadtxt('Storage_AI_maxcell_random.txt')
    data_maxcell_clockwise = np.loadtxt('Storage_AI_maxcell_clockwise.txt')
   

    plt.figure(1)
    
    plt.hist(data_maxcell_random, label='random strategy', bins=15, color=random_color)
    plt.hist(data_maxcell_clockwise, label='clockwise strategy', bins=15, color=clockwise_color)
    plt.legend(loc='upper right')
    plt.title("Distribution of max score")
    plt.ylabel("Number of apparition among 300 000 try")
    plt.xlabel("Max cell")
    plt.savefig('AI_maxcell_randomvsclockwise.pdf')
    plt.show()
    

    










# else:

#     Data_score_up = np.loadtxt('./Data_storage/Storage_AI_score_up.txt')
#     Data_score_down = np.loadtxt('./Data_storage/Storage_AI_score_down.txt')
#     Data_score_left = np.loadtxt('./Data_storage/Storage_AI_score_left.txt')
#     Data_score_right = np.loadtxt('./Data_storage/Storage_AI_score_right.txt')


#     Mean_storage_up = (1/np.arange(1, len(Data_score_up)+1)) * np.cumsum(Data_score_up)
#     Mean_storage_down = (1/np.arange(1, len(Data_score_down)+1)) * np.cumsum(Data_score_down)
#     Mean_storage_left = (1/np.arange(1, len(Data_score_left)+1)) * np.cumsum(Data_score_left)
#     Mean_storage_right = (1/np.arange(1, len(Data_score_right)+1)) * np.cumsum(Data_score_right)





#     plt.figure()
#     plt.plot(Mean_storage_up, color='#FF8C00', label='up movement')
#     plt.plot(Mean_storage_left, color='#DC143C', label='left movement')
#     plt.plot(Mean_storage_right, color='#6495ED', label='right movement')
#     plt.plot(Mean_storage_down, color='#da70d6', label='down movement')
#     plt.legend()
#     plt.xlim(0, 1500)
#     plt.ylim(100,300)
#     # plt.plot(Mean_storage, color='#FF8C00')
#     # plt.label('random movement')
#     plt.savefig('./Data_storage/AI_score_onemovement.pdf')
#     plt.show()

