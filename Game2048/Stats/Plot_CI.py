""" Confidence intervals plots

    This script construct the confidence interval for all the data.
    Using the data set already loaded in the package and the data that you get with Build_CI script.
    The plots are stored in this dirrectory in svg format.

 """

import numpy as np
import matplotlib.pyplot as plt

# Loading data set

random_color = '#8A2BE2'
clock_color = '#FF8C00'
opp_color = '#6495ED'
adj_color = '#DC143C'

score_random = np.loadtxt('Game2048/Stats/Data/Storage_AI_score_random.txt')
score_clock = np.loadtxt('Game2048/Stats/Data/Storage_AI_score_clockwise.txt')
score_opp = np.loadtxt('Game2048/Stats/Data/Storage_AI_score_opposite.txt')
score_adj = np.loadtxt('Game2048/Stats/Data/Storage_AI_score_adjacent.txt')

Mean_random = (1/np.arange(1, len(score_random)+1)) * np.cumsum(score_random)
Mean_clock = (1/np.arange(1, len(score_clock)+1)) * np.cumsum(score_clock)
Mean_opp = (1/np.arange(1, len(score_opp)+1)) * np.cumsum(score_opp)
Mean_adj = (1/np.arange(1, len(score_adj)+1)) * np.cumsum(score_adj)


inf_random = np.loadtxt('Game2048/Stats/Data/Empirical_mean_inf_random.txt')
sup_random = np.loadtxt('Game2048/Stats/Data/Empirical_mean_sup_random.txt')

inf_clock = np.loadtxt('Game2048/Stats/Data/Empirical_mean_inf_clockwise.txt')
sup_clock = np.loadtxt('Game2048/Stats/Data/Empirical_mean_sup_clockwise.txt')

inf_opp = np.loadtxt('Game2048/Stats/Data/Empirical_mean_inf_opposite.txt')
sup_opp = np.loadtxt('Game2048/Stats/Data/Empirical_mean_sup_opposite.txt')

inf_adj = np.loadtxt('Game2048/Stats/Data/Empirical_mean_inf_adjacent.txt')
sup_adj = np.loadtxt('Game2048/Stats/Data/Empirical_mean_sup_adjacent.txt')

x = np.arange(0, len(Mean_random)-2, 1)

# Random plot

plt.figure()
plt.plot(x, Mean_random[2:300000],
         color=random_color, label='Random strategy')
plt.plot(x, inf_random, '--',
         color="black", label='confidence interval 95%')
plt.plot(x, sup_random, '--',
         color="black")
plt.fill_between(x, inf_random, sup_random,
                 color='#D3D3D3')
plt.ylim(1000, 1200)
plt.xlim(0, 300000)
plt.title("Average point gain with random strategy")
plt.xlabel("number of data")
plt.ylabel("Empirical mean")
plt.legend()
plt.savefig('Game2048/Stats/Your_result/Random_strategy_meanCI.svg', format='svg')
plt.show()

# Clockwise plot

plt.figure()
plt.plot(x, Mean_clock[2:300000],
         color=clock_color, label='Clockwise strategy')
plt.plot(x, inf_clock, '--',
         color="black", label='confidence interval 95%')
plt.plot(x, sup_clock, '--',
         color="black")
plt.fill_between(x, inf_clock, sup_clock,
                 color='#D3D3D3')
plt.ylim(2200, 2400)
plt.xlim(0, 300000)
plt.title("Average point gain with clockwise strategy")
plt.xlabel("number of data")
plt.ylabel("Empirical mean")
plt.legend()
plt.savefig('Game2048/Stats/Your_result/Clockwise_strategy_meanCI.svg', format='svg')
plt.show()

# Opposite plot

plt.figure()
plt.plot(x, Mean_opp[2:300000], color=opp_color, label='Opposite strategy')
plt.plot(x, inf_opp, '--',
         color="black", label='confidence interval 95%')
plt.plot(x, sup_opp, '--',
         color="black")
plt.fill_between(x, inf_opp, sup_opp,
                 color='#D3D3D3')
plt.ylim(70, 100)
plt.xlim(0, 300000)
plt.title("Average point gain with opposite strategy")
plt.xlabel("number of data")
plt.ylabel("Empirical mean")
plt.legend()
plt.savefig('Game2048/Stats/Your_result/Opposite_strategy_meanCI.svg', format='svg')
plt.show()

# Adjacent plot

plt.figure()
plt.plot(x, Mean_adj[2:300000],
         color=adj_color, label='Adjacent strategy')
plt.plot(x, inf_adj, '--',
         color="black", label='confidence interval 95%')
plt.plot(x, sup_adj, '--',
         color="black")
plt.fill_between(x, inf_adj, sup_adj,
                 color='#D3D3D3')
plt.ylim(100, 135)
plt.xlim(0, 300000)
plt.title("Average point gain with adjacent strategy")
plt.xlabel("number of data")
plt.ylabel("Empirical mean")
plt.legend()
plt.savefig('Game2048/Stats/Your_result/Adjacent_strategy_meanCI.svg', format='svg')
plt.show()
