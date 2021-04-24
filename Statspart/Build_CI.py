""" Confidence interval builder """

import numpy as np
from numba import jit

# Load data get with Make_graph
print('Load data')

score_opp = np.loadtxt('Storage_AI_score_opposite.txt')
score_adj = np.loadtxt('Storage_AI_score_adjacent.txt')
score_random = np.loadtxt('Storage_AI_score_random.txt')
score_clock = np.loadtxt('Storage_AI_score_clockwise.txt')

# Get empirical mean and empirical standard deviation
empirical_mean_opp = np.mean(score_opp)
empirical_mean_adj = np.mean(score_adj)
empirical_mean_random = np.mean(score_random)
empirical_mean_clock = np.mean(score_clock)

print('-------------------------------------------------------------------')
print('\n')
print(f'Empirical mean of opposite strategy score is {empirical_mean_opp}')
print(f'Empirical mean of adjacent strategy score is {empirical_mean_adj}')
print(f'Empirical mean of random strategy score is {empirical_mean_random}')
print(f'Empirical mean of clockwise strategy score is {empirical_mean_clock}')


Var_random = 1/300000 * sum((score_random - empirical_mean_random)**2)
Var_clock = 1/300000 * sum((score_clock - empirical_mean_clock)**2)
Var_adj = 1/300000 * sum((score_adj - empirical_mean_adj)**2)
Var_opp = 1/300000 * sum((score_opp - empirical_mean_opp)**2)

print('----------------------------------------------------------------- \n')


sigma_random = np.sqrt(Var_random)
sigma_clock = np.sqrt(Var_clock)
sigma_adj = np.sqrt(Var_adj)
sigma_opp = np.sqrt(Var_opp)

print(f'Standard deviation of opposite strategy score is {sigma_opp}')
print(f'Standard deviation of adjacent strategy score is {sigma_adj}')
print(f'Standard deviation of random strategy score is {sigma_random}')
print(f'Standard deviation of clockwise strategy score is {sigma_clock}')

print('----------------------------------------------------------------- \n')


# Compute empirical mean for all data set
Mean_random = (1/np.arange(1, len(score_random)+1)) * np.cumsum(score_random)
Mean_clock = (1/np.arange(1, len(score_clock)+1)) * np.cumsum(score_clock)
Mean_opp = (1/np.arange(1, len(score_opp)+1)) * np.cumsum(score_opp)
Mean_adj = (1/np.arange(1, len(score_adj)+1)) * np.cumsum(score_adj)

# Function that allow us to build confidence interval of the mean
# estimation with Law of large numbers


@jit(nopython=True)
def Confidence_interval(mu, sigma, i):
    """
    
    """
    borne_inf = (mu - ((1.96 * sigma)/np.sqrt(i)))
    born_sup = (mu + ((1.96 * sigma)/np.sqrt(i)))
    return borne_inf, born_sup


@jit(nopython=True)
def Construct_CI(score_storage, mean_storage, nb_data=300000):
    """ 
    Generates upper and lower bounds of the mean score confidence interval in 
    anticipation of printing the confidence interval
    """
    inf = []
    sup = []

    for i in range(2, nb_data):

        Variance = 1/(i-1) * np.sum((score_storage[2:i] - mean_storage[i])**2)
        sigma = np.sqrt(Variance)
        a, b = Confidence_interval(mean_storage[i], sigma, i)
        inf.append(a)
        sup.append(b)

    return inf, sup


# Print Confidence interval

infopp, supopp = Confidence_interval(empirical_mean_opp,
                                     sigma_opp, 300000)
infadj, supadj = Confidence_interval(empirical_mean_adj,
                                     sigma_adj, 300000)
infrandom, suprandom = Confidence_interval(empirical_mean_random,
                                           sigma_random, 300000)
infclock, supclock = Confidence_interval(empirical_mean_clock,
                                         sigma_clock, 300000)

print(f'Random CI [{infrandom}; {suprandom}] \n')
print(f'Clockwise CI [{infclock}; {supclock}] \n')
print(f'Adjacent CI [{infadj}; {supadj}] \n')
print(f'Opposite CI [{infopp}; {supopp}] \n')
print('\n')
print('start computation')
print('Loading [XX--------]')

# Save data to construct a plot

inf_clock, sup_clock = Construct_CI(score_clock,
                                    Mean_clock)

np.savetxt('Empirical_mean_inf_clockwise.txt', inf_clock)
np.savetxt('Empirical_mean_sup_clockwise.txt', sup_clock)

print('Loading [XXXX------]')

inf_random, sup_random = Construct_CI(score_random,
                                      Mean_random)
np.savetxt('Empirical_mean_inf_random.txt', inf_random)
np.savetxt('Empirical_mean_sup_random.txt', sup_random)

print('Loading [XXXXXX----]')

inf_opp, sup_opp = Construct_CI(score_opp,
                                Mean_opp)
np.savetxt('Empirical_mean_inf_opposite.txt', inf_opp)
np.savetxt('Empirical_mean_sup_opposite.txt', sup_opp)

print('Loading [XXXXXXXX--]')

inf_adj, sup_adj = Construct_CI(score_adj,
                                Mean_adj)
np.savetxt('Empirical_mean_inf_adjacent.txt', inf_adj)
np.savetxt('Empirical_mean_sup_adjacent.txt', sup_adj)

print('Loading [XXXXXXXXXX]')
print('done')
