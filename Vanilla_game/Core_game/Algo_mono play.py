import random
import numpy as np
import Main
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

just_calcul = True



if just_calcul is False:

    stockage_score_random = []
    stockage_score_clockwise = []
    stockage_maxcell_random = []
    stockage_maxcell_clockwise = []
    for i in range(300000):
        AI_one = Main.Game_2048()
        AI_one.random_2048()
        AI_one.maxcell_find()
        stockage_maxcell_random.append(AI_one.maxcell)
        stockage_score_random.append(AI_one.score)

        AI_two = Main.Game_2048()
        AI_two.clockwise_2048()
        AI_two.maxcell_find()
        stockage_maxcell_clockwise.append(AI_two.maxcell)
        stockage_score_clockwise.append(AI_two.score)
        print(i)


    data_random = np.array(stockage_score_random)
    data_clockwise = np.array(stockage_score_clockwise)

    np.savetxt('Vanilla_game/Data_storage/Storage_AI_score_random.txt', data_random)
    np.savetxt('Vanilla_game/Data_storage/Storage_AI_score_clockwise.txt', data_clockwise)
    np.savetxt('Vanilla_game/Data_storage/Storage_AI_maxcell_random.txt', stockage_maxcell_random)
    np.savetxt('Vanilla_game/Data_storage/Storage_AI_maxcell_clockwise.txt',  stockage_maxcell_clockwise)



else:

    data_score_random = np.loadtxt('Vanilla_game/Data_storage/Storage_AI_score_random.txt')
    data_score_clockwise = np.loadtxt('Vanilla_game/Data_storage/Storage_AI_score_clockwise.txt')

    Mean_storage_random = (1/np.arange(1, len(data_score_random)+1)) * np.cumsum(data_score_random)
    Mean_storage_clockwise = (1/np.arange(1, len(data_score_clockwise)+1)) * np.cumsum(data_score_clockwise)

    plt.figure()
    plt.plot(Mean_storage_random, color='#FF8C00', label='Random movement')
    plt.plot(Mean_storage_clockwise, color='#DC143C', label='Clockwise movement')
    plt.title("Empirical mean convergence")
    plt.legend()
    plt.xlabel("Number of data")
    plt.ylabel("Empirical mean")
    plt.xlim(0, 1500)
    plt.ylim(700,1300)
    plt.savefig('Vanilla_game/Data_storage/AI_score.pdf')
    plt.show()


    d = {'Random strategie': data_score_random, 'Clockwise strategie': data_score_clockwise}
    df = pd.DataFrame(d)
    plt.figure()
    sns.kdeplot(data_score_random, bw_adjust=0.1, legend=False)
    sns.kdeplot(data_score_clockwise, bw_adjust=0.1)
    plt.title("Distribution of score with random et clockwise strategies")
    plt.xlabel("score")
    plt.savefig('Vanilla_game/Data_storage/AI_distribution.pdf')


    plt.show()


    data_maxcell_random = np.loadtxt('Vanilla_game/Data_storage/Storage_AI_maxcell_random.txt')
    data_maxcell_clockwise = np.loadtxt('Vanilla_game/Data_storage/Storage_AI_maxcell_clockwise.txt')
   

    plt.figure(1)
    
    plt.hist([data_maxcell_random, data_maxcell_clockwise], label=['Random strategie', 'Clockwise strategie'])
    plt.legend(loc='upper right')
    plt.title("Distribution of max score")
    plt.ylabel("Number of apparition among 300 000 try")
    plt.xlabel("Max cell")
    plt.savefig('Vanilla_game/Data_storage/AI_maxcell.pdf')
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
#     # plt.label('Random movement')
#     plt.savefig('./Data_storage/AI_score_onemovement.pdf')
#     plt.show()

