import random
import numpy as np
from Game2048.Main import Game_2048
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

just_plot = True


# DON'T RUN 

if just_plot is False:

    stockage_score_opposite = []
    stockage_score_adjacent = []
    stockage_maxcell_opposite = []
    stockage_maxcell_adjacent = []
    for i in range(300000):
        AI_one = Game_2048()
        AI_one.opposite_2048()
        AI_one.maxcell_find()
        stockage_maxcell_opposite.append(AI_one.maxcell)
        stockage_score_opposite.append(AI_one.score)

        AI_two = Game_2048()
        AI_two.adjacent_2048()
        AI_two.maxcell_find()
        stockage_maxcell_adjacent.append(AI_two.maxcell)
        stockage_score_adjacent.append(AI_two.score)
        print(i)


    data_opposite = np.array(stockage_score_opposite)
    data_adjacent = np.array(stockage_score_adjacent)

    np.savetxt('Storage_AI_score_opposite.txt', data_opposite)
    np.savetxt('Storage_AI_score_adjacent.txt', data_adjacent)
    np.savetxt('Storage_AI_maxcell_opposite.txt', stockage_maxcell_opposite)
    np.savetxt('Storage_AI_maxcell_adjacent.txt', stockage_maxcell_adjacent)



else:


    opposite_color = '#8A2BE2'
    adjacent_color = '#FF8C00'
    data_score_opposite = np.loadtxt('Storage_AI_score_opposite.txt')
    data_score_adjacent = np.loadtxt('Storage_AI_score_adjacent.txt')

    Mean_storage_opposite = (1/np.arange(1, len(data_score_opposite) + 1)) * np.cumsum(data_score_opposite)
    Mean_storage_adjacent = (1/np.arange(1, len(data_score_adjacent) + 1)) * np.cumsum(data_score_adjacent)



    empirical_mean_opposite = Mean_storage_opposite[len(Mean_storage_opposite) - 1]
    empirical_mean_adjacent = Mean_storage_adjacent[len(Mean_storage_adjacent) - 1]

    print(f'Empirical mean for opposite strategie is {empirical_mean_opposite}')
    print(f'Empirical mean for opposite adjacent is {empirical_mean_adjacent}')

    plt.figure()
    plt.plot(Mean_storage_opposite, color=opposite_color, label='opposite movement')
    plt.plot(Mean_storage_adjacent, color=adjacent_color, label='adjacent movement')
    plt.title("Empirical mean convergence")
    plt.legend()
    plt.xlabel("Number of data")
    plt.ylabel("Empirical mean")
    plt.xlim(0, 1500)
    plt.ylim(0, 400)
    plt.savefig('AI_score_oppositevsadjacent.svg', format = 'svg')
    plt.show()


    d = {'opposite strategy': data_score_opposite, 'adjacent strategy': data_score_adjacent}
    df = pd.DataFrame(d)
    plt.figure()
    sns.kdeplot(data_score_opposite, bw_adjust=0.1, legend=True, color=opposite_color)
    sns.kdeplot(data_score_adjacent, bw_adjust=0.1, legend=True, color=adjacent_color)
    # plt.vlines(empirical_mean_opposite, 0, 0.00125, colors='black')
    # plt.vlines(empirical_mean_adjacent, 0, 0.00125, colors='black')
    plt.legend(labels=['opposite strategy', 'adjacent strategy'])
    plt.title("Distribution of score with opposite et adjacent strategies")
    plt.xlabel("Score")
    plt.xlim(0, 400)
    plt.savefig('AI_distribution_oppositevsadjacent.svg',format = 'svg')


    plt.show()


    data_maxcell_opposite = np.loadtxt('Storage_AI_maxcell_opposite.txt')
    data_maxcell_adjacent = np.loadtxt('Storage_AI_maxcell_adjacent.txt')
   

    plt.figure(1)
    
    plt.hist(data_maxcell_opposite, label='opposite strategy', bins=15, color=opposite_color)
    plt.hist(data_maxcell_adjacent, label='adjacent strategy', bins=15, color=adjacent_color)
    plt.legend(loc='upper right')
    plt.title("Distribution of max score")
    plt.ylabel("Number of apparition among 300 000 try")
    plt.xlabel("Max cell")
    plt.savefig('AI_maxcell_oppositevsadjacent.svg', format = 'svg')
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
#     # plt.label('opposite movement')
#     plt.savefig('./Data_storage/AI_score_onemovement.pdf')
#     plt.show()

