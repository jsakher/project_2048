import Game2048.Main as Main
import random
import time

# First try AI versus
# empirical values

random_empirical_mean = 1000
clockwise_empirical_mean = 2000
opposite_empirical_mean = 100
adjacent_empirical_mean = 200
# %%


def launch_versus():
    AI_one = Main.Game_2048()
    AI_two = Main.Game_2048()
   
    AI_one.newcell_start()
    AI_one.newcell()
    AI_two.newcell_start()
    AI_two.newcell()
    return AI_one, AI_two

def set_random_position():
    seed = random.random()
    if seed > 0.5:
        two_opposite = ['z', 's']
        two_adjacent = ['z', 'q']
    if seed <= 0.5:
        two_opposite = ['q', 'd']
        two_adjacent = ['s', 'd']
    
    return two_opposite, two_adjacent

def scoreboard(grid1, grid2, strategy1, strategy2):
    print('--------------------------------------------------------------------------------------------------------------------')
    average1 = ''
    average2 = ''
    strategy_win = ''

    if grid1.score < grid2.score:
        strategy_win = strategy2
    else:
        strategy_win = strategy1
    if(grid1.score < grid2.score):
        print(f"AI_two win this game, {strategy2} strategy won this time,")
        print('')
    else:
        print(f"AI_one win this game, {strategy1} strategy won this time,")
        print('')


    if grid1.score > random_empirical_mean and strategy1 == 'random':
        average1 = ", lucky score !"
    if grid2.score > random_empirical_mean and strategy2 == 'random':
        average2 = ", lucky score !"
    
    if grid1.score > clockwise_empirical_mean and strategy1 == 'clockwise':
        average1 = ", lucky score !"
    if grid2.score > clockwise_empirical_mean and strategy2 == 'clockwise':
        average2 = ", lucky score !"

    print(f"The final score for AI_one is {grid1.score}{average1}")
    print(f"The final score for AI_two is {grid2.score}{average2}")
    print('')

    if strategy_win == 'clockwise':
        print(f'The empirical mean with the {strategy_win} strategy is {clockwise_empirical_mean} and the empirical variance is ')
    if strategy_win == 'random':
        print(f'The empirical mean with the {strategy_win} strategy is {random_empirical_mean} and the empirical variance is ')

    if strategy_win == 'opposite':
        print(f'The empirical mean with the {strategy_win} strategy is {opposite_empirical_mean} and the empirical variance is ')

    if strategy_win == 'adjacent':
        print(f'The empirical mean with the {strategy_win} strategy is {adjacent_empirical_mean} and the empirical variance is ')
    print('--------------------------------------------------------------------------------------------------------------------')


def state_game2(grid1, grid2, x="", y="", strategy1="", strategy2=""):
    ''' Display the grid's state '''
    print("--------------------------------------------------------------------")
    print(f'AI_one play: {x}                          AI_two play: {y}')
    print("\n")
    print(f"{grid1.grid[0]}                            {grid2.grid[0]}")
    print(f"{grid1.grid[1]}                            {grid2.grid[1]}")
    print(f"{grid1.grid[2]}                            {grid2.grid[2]}")
    print(f"{grid1.grid[3]}                            {grid2.grid[3]}")
    print(f"AI_one score is {grid1.score}                      AI_two score is {grid2.score}")
    print(f"AI_one play {strategy1} strategy            AI_two play {strategy2} strategy")

    return('------------')


def Versus(strategy1='random', strategy2='random', skip=True, speed=0.5):

  

    two_opposite, two_adjacent = set_random_position()
    AI_one, AI_two = launch_versus()

    if skip is False:
        state_game2(AI_one, AI_two)
    
    x = random.choice(AI_one.directions)
    y = random.choice(AI_two.directions)
    

    block_game1 = 0
    block_game2 = 0
    nb_movement = 0
    movement_play1 = 0
    movement_play2 = 0

    while(AI_one.status or AI_two.status):
        

        if strategy1 == 'random':
            x = random.choice(AI_one.directions)
        if strategy2 == 'random':
            y = random.choice(AI_two.directions)

        if strategy1 == 'clockwise':
            x = AI_one.directions[AI_one.directions.index(x) - 1]
        if strategy2 == 'clockwise':
            y = AI_two.directions[AI_two.directions.index(y) - 1]

        if strategy1 == 'opposite':
            x = two_opposite[movement_play1]
            movement_play1 = (movement_play1 + 1)%2

        if strategy2 == 'opposite':
            y = two_opposite[movement_play2]
            movement_play2 = (movement_play2 + 1)%2
        
        if strategy1 == 'adjacent':
            x = two_adjacent[movement_play1]
            movement_play1 = (movement_play1 + 1)%2

        if strategy2 == 'adjacent':
            y = two_adjacent[movement_play2]
            movement_play2 = (movement_play2 + 1)%2
         


        grid_test1 = AI_one.grid
        grid_test2 = AI_two.grid

        if (x.upper() == 'D'):
            AI_one.right_movement()
        if (x.upper() == 'Z'):
            AI_one.up_movement()
        if (x.upper() == 'S'):
            AI_one.down_movement()
        if (x.upper() == 'Q'):
            AI_one.left_movement()
        if (y.upper() == 'D'):
            AI_two.right_movement()
        if (y.upper() == 'Z'):
            AI_two.up_movement()
        if (y.upper() == 'S'):
            AI_two.down_movement()
        if (y.upper() == 'Q'):
            AI_two.left_movement()

        AI_one.stop_game()
        AI_two.stop_game()
        
        
        if AI_one.status and AI_one.grid != grid_test1:
            AI_one.newcell()
        if AI_two.status and AI_two.grid != grid_test2:
            AI_two.newcell()

        if strategy1 == 'opposite' or strategy1 == 'adjacent':
            if AI_one.grid == grid_test1:
                block_game1 += 1
            if block_game1 > 3:
                AI_one.status = False

        if strategy2 == 'opposite' or strategy2 == 'adjacent' :    
            if AI_two.grid == grid_test2:
                block_game2 += 1
            if block_game2 > 3:
                AI_two.status = False
        if skip is False:
            state_game2(AI_one, AI_two, x, y, strategy1, strategy2)
            time.sleep(speed)
        nb_movement += 1

        if nb_movement > 1000:
            AI_one.status = False
            AI_two.status = False

    scoreboard(AI_one, AI_two, strategy1, strategy2)


# Versus('random', 'adjacent', skip=True)

