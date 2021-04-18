import Game2048.Main as Main
import random
import time

# First try AI versus
# empirical values

random_emperical_mean = 1000
clockwise_empirical_mean = 2000
opposite_empirical_mean = 100
adjacent_empirical_mean = 200
# %%


def lauch_versus():
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

def scorebord(grid1, grid2, strategie1, strategie2):
    print('--------------------------------------------------------------------------------------------------------------------')
    average1 = ''
    average2 = ''
    strategie_win = ''

    if grid1.score < grid2.score:
        strategie_win = strategie2
    else:
        strategie_win = strategie1
    if(grid1.score < grid2.score):
        print(f"AI_two win this game, {strategie2} strategie won this time,")
        print('')
    else:
        print(f"AI_one win this game, {strategie1} strategie won this time,")
        print('')


    if grid1.score > random_emperical_mean and strategie1 == 'random':
        average1 = ", lucky score !"
    if grid2.score > random_emperical_mean and strategie2 == 'random':
        average2 = ", lucky score !"
    
    if grid1.score > clockwise_empirical_mean and strategie1 == 'clockwise':
        average1 = ", lucky score !"
    if grid2.score > clockwise_empirical_mean and strategie2 == 'clockwise':
        average2 = ", lucky score !"

    print(f"The final score for AI_one is {grid1.score}{average1}")
    print(f"The final score is AI_two is {grid2.score}{average2}")
    print('')

    if strategie_win == 'clockwise':
        print(f'The empirical mean with the {strategie_win} strategie is {clockwise_empirical_mean} and the empirical variance is ')
    if strategie_win == 'random':
        print(f'The empirical mean with the {strategie_win} strategie is {random_emperical_mean} and the empirical variance is ')

    if strategie_win == 'opposite':
        print(f'The empirical mean with the {strategie_win} strategie is {opposite_empirical_mean} and the empirical variance is ')

    if strategie_win == 'adjacent':
        print(f'The empirical mean with the {strategie_win} strategie is {adjacent_empirical_mean} and the empirical variance is ')
    print('--------------------------------------------------------------------------------------------------------------------')


def state_game2(grid1, grid2, x="", y="" , strategie1="", strategie2=""):
    ''' Display the grid's state '''
    print("--------------------------------------------------------------------")
    print(f'AI_one play: {x}                          AI_two play: {y}')
    print("\n")
    print(f"{grid1.grid[0]}                            {grid2.grid[0]}")
    print(f"{grid1.grid[1]}                            {grid2.grid[1]}")
    print(f"{grid1.grid[2]}                            {grid2.grid[2]}")
    print(f"{grid1.grid[3]}                            {grid2.grid[3]}")
    print(f"AI_one score is {grid1.score}                      AI_two score is {grid2.score}")
    print(f"AI_one play {strategie1} stratgie             AI_two play {strategie2} strategie")

    return('------------')


def Versus(strategie1='random', strategie2='random', skip=True, speed = 0.5):

  

    two_opposite , two_adjacent = set_random_position()
    AI_one, AI_two = lauch_versus()

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
        

        if strategie1 == 'random':
            x = random.choice(AI_one.directions)
        if strategie2 == 'random':
            y = random.choice(AI_two.directions)

        if strategie1 == 'clockwise':
            x = AI_one.directions[AI_one.directions.index(x) - 1]
        if strategie2 == 'clockwise':
            y = AI_two.directions[AI_two.directions.index(y) - 1]

        if strategie1 == 'opposite':
            x = two_opposite[movement_play1]
            movement_play1 = (movement_play1 + 1)%2

        if strategie2 == 'opposite':
            y = two_opposite[movement_play2]
            movement_play2 = (movement_play2 + 1)%2
        
        if strategie1 == 'adjacent':
            x = two_adjacent[movement_play1]
            movement_play1 = (movement_play1 + 1)%2

        if strategie2 == 'adjacent':
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

        if strategie1 == 'opposite' or strategie1 == 'adjacent':
            if AI_one.grid == grid_test1:
                block_game1 += 1
            if block_game1 > 3:
                AI_one.status = False

        if strategie2 == 'opposite' or strategie2 == 'adjacent' :    
            if AI_two.grid == grid_test2:
                block_game2 += 1
            if block_game2 > 3:
                AI_two.status = False
        if skip is False:
            state_game2(AI_one, AI_two, x, y, strategie1, strategie2)
            time.sleep(speed)
        nb_movement += 1

        if nb_movement > 1000:
            AI_one.status = False
            AI_two.status = False

    scorebord(AI_one, AI_two, strategie1, strategie2)


# Versus('random', 'adjacent', skip=True)

