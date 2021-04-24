import random
import numpy as np
from Game2048.game.Main import Game_2048
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

just_plot = True


# DON'T RUN 
def plot_maker(just_plot, strategy1, strategy2, n):

    if just_plot is False:

        stockage_score_strategy1 = []
        stockage_score_strategy2 = []
        stockage_maxcell_strategy1 = []
        stockage_maxcell_strategy2 = []
        for i in range(n):
            AI_one = Game_2048()
            getattr(AI_one, strategy1)()  
            AI_one.maxcell_find()
            stockage_maxcell_strategy1.append(AI_one.maxcell)
            stockage_score_strategy1.append(AI_one.score)

            AI_two = Game_2048()
            getattr(AI_two, strategy2)()
            AI_two.maxcell_find()
            stockage_maxcell_strategy2.append(AI_two.maxcell)
            stockage_score_strategy2.append(AI_two.score)
            print(i)


        data_strategy1 = np.array(stockage_score_strategy1)
        data_strategy2 = np.array(stockage_score_strategy2)

        np.savetxt(f'./try/Storage_AI_score_{strategy1}.txt', data_strategy1)
        np.savetxt(f'./try/Storage_AI_score_{strategy2}.txt', data_strategy2)
        np.savetxt(f'./try/Storage_AI_maxcell_{strategy1}.txt', stockage_maxcell_strategy1)
        np.savetxt(f'./try/Storage_AI_maxcell_{strategy2}.txt', stockage_maxcell_strategy2)



    else:


        strategy1_color = '#8A2BE2'
        strategy2_color = '#FF8C00'
        data_score_strategy1 = np.loadtxt(f'./try/Storage_AI_score_{strategy1}.txt')
        data_score_strategy2 = np.loadtxt(f'./try/Storage_AI_score_{strategy2}.txt')

        Mean_storage_strategy1 = (1/np.arange(1, len(data_score_strategy1) + 1)) * np.cumsum(data_score_strategy1)
        Mean_storage_strategy2 = (1/np.arange(1, len(data_score_strategy2) + 1)) * np.cumsum(data_score_strategy2)



        empirical_mean_strategy1 = Mean_storage_strategy1[len(Mean_storage_strategy1) - 1]
        empirical_mean_strategy2 = Mean_storage_strategy2[len(Mean_storage_strategy2) - 1]

        print(f'Empirical mean for strategy1 strategie is {empirical_mean_strategy1}')
        print(f'Empirical mean for strategy1 strategy2 is {empirical_mean_strategy2}')

        plt.figure()
        plt.plot(Mean_storage_strategy1, color=strategy1_color, label=f'{strategy1} movement')
        plt.plot(Mean_storage_strategy2, color=strategy2_color, label=f'{strategy2} movement')
        plt.title("Empirical mean convergence")
        plt.legend()
        plt.xlabel("Number of data")
        plt.ylabel("Empirical mean")
        plt.xlim(0, 1500)
        if ((strategy1 == strategy1 and strategy2 == strategy2) or (strategy1 == strategy2 and strategy2 == strategy1)):
            plt.ylim(0, 400)
        else:
            plt.ylim(0, 4000)
        plt.savefig(f'./try/AI_score_{strategy1}vs{strategy2}.svg', format = 'svg')
        plt.show()


        d = {f'{strategy1} strategy': data_score_strategy1, f'{strategy2} strategy': data_score_strategy2}
        df = pd.DataFrame(d)
        plt.figure()
        sns.kdeplot(data_score_strategy1, bw_adjust=0.1, legend=True, color=strategy1_color)
        sns.kdeplot(data_score_strategy2, bw_adjust=0.1, legend=True, color=strategy2_color)
        # plt.vlines(empirical_mean_strategy1, 0, 0.00125, colors='black')
        # plt.vlines(empirical_mean_strategy2, 0, 0.00125, colors='black')
        plt.legend(labels=[f'{strategy1} strategy', f'{strategy2} strategy'])
        plt.title(f"Distribution of score with {strategy1} and {strategy2} strategies")
        plt.xlabel("Score")
        plt.xlim(0, 400)
        plt.savefig(f'./try/AI_distribution_{strategy1}vs{strategy2}.svg',format = 'svg')


        plt.show()


        data_maxcell_strategy1 = np.loadtxt(f'./try/Storage_AI_maxcell_{strategy1}.txt')
        data_maxcell_strategy2 = np.loadtxt(f'./try/Storage_AI_maxcell_{strategy2}.txt')
   

        plt.figure(1)
    
        plt.hist(data_maxcell_strategy1, label=f'{strategy1} strategy', bins=15, color=strategy1_color)
        plt.hist(data_maxcell_strategy2, label=f'{strategy2} strategy', bins=15, color=strategy2_color)
        plt.legend(loc='upper right')
        plt.title("Distribution of max score")
        plt.ylabel("Number of apparition among 300 000 try")
        plt.xlabel("Max cell")
        plt.savefig(f'./try/AI_maxcell_{strategy1}vs{strategy2}.svg', format = 'svg')
        plt.show()
    

plot_maker(False, opposite_2048, adjacent_2048, 100)  











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
#     # plt.label('strategy1 movement')
#     plt.savefig('./Data_storage/AI_score_onemovement.pdf')
#     plt.show()

