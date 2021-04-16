import Main
import random


# First try AI versus

# %%

def state_game2(grid1, grid2):
    ''' Display the grid's state '''
    print("--------------------------------------------------------------------")
    print("\n")
    print(f"{grid1.grid[0]}                            {grid2.grid[0]}")
    print(f"{grid1.grid[1]}                            {grid2.grid[1]}")
    print(f"{grid1.grid[2]}                            {grid2.grid[2]}")
    print(f"{grid1.grid[3]}                            {grid2.grid[3]}")
    print(f"AI_one score is {grid1.score}                      AI_two score is {grid2.score}")
    
    
    return('------------')

import time
def Versus(strategie1='random', strategie2='random', skip=True):
    
    average1 = ""
    average2 = ""

    directions = ['z', 'q', 's', 'd']
    AI_one = Main.Game_2048()
    AI_two = Main.Game_2048()
    AI_tree = Main.Game_2048()

    AI_one.newcell_start()
    AI_one.newcell()
    

    AI_two.newcell_start()
    AI_two.newcell()

    AI_tree.newcell_start()
    state_game2(AI_one, AI_two)
    Stop_versus = True

    while(AI_one.status or AI_two.status):
        
        x = random.choice(directions)
        y = random.choice(directions)
        grid_test = AI_one.grid
        grid_test = AI_two.grid

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
        
        
        if AI_one.status and AI_one.grid != grid_test:
            AI_one.newcell()
        if AI_two.status and AI_one.grid != grid_test:
            AI_two.newcell()
        if skip is False:
            time.sleep(0.5)
            state_game2(AI_one,AI_two)
        
    if(AI_one.score < AI_two.score):
        print(f"AI_two win this game, {strategie2} strategie won this time")
    else:
        print(f"AI_one win this game, {strategie1} strategie won this time")
    if AI_one.score > 730:
        average1 = ", lucky score !"
    if AI_two.score > 730:
        average2 = ", lucky score !"

    print(f"The final score for AI_one is {AI_one.score}{average1}")
    print(f"The final score is AI_two is {AI_two.score}{average2}")






def Versus2(strategie1='random', strategie2='random', skip=True):
    
    average1 = ""
    average2 = ""

    directions = ['z', 'q', 's', 'd']
    AI_one = Main.Game_2048()
    AI_two = Main.Game_2048()
    

    AI_one.newcell_start()
    AI_one.newcell()

    AI_two.newcell_start()
    AI_two.newcell()

    state_game2(AI_one, AI_two)
    Stop_versus = True
    y = random.choice(AI_two.directions)
    block_game = 0



    while(AI_one.status or AI_two.status):
        
        x = random.choice(directions)
        y = AI_two.directions[AI_two.directions.index(y) - 2]
        grid_test = AI_one.grid
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
        
        
        if AI_one.status and AI_one.grid != grid_test:
            AI_one.newcell()
        if AI_two.status and AI_one.grid != grid_test:
            AI_two.newcell()
        if skip is False:
            time.sleep(0.10)
            print(y)
            state_game2(AI_one,AI_two)
        if AI_two.grid == grid_test2:
            block_game += 1
        if block_game > 3:
            AI_two.status = False
            print(block_game)
        
    if(AI_one.score < AI_two.score):
        print(f"AI_two win this game, {strategie2} strategie won this time")
    else:
        print(f"AI_one win this game, {strategie1} strategie won this time")
    if AI_one.score > 730:
        average1 = ", lucky score !"
    if AI_two.score > 730:
        average2 = ", lucky score !"

    print(f"The final score for AI_one is {AI_one.score}{average1}")
    print(f"The final score is AI_two is {AI_two.score}{average2}")




def Versus3(strategie1='random', strategie2='random', skip=True):
    
    average1 = ""
    average2 = ""

    directions = ['z', 'q', 's', 'd']
    AI_one = Main.Game_2048()
    AI_two = Main.Game_2048()
    

    AI_one.newcell_start()
    AI_one.newcell()

    AI_two.newcell_start()
    AI_two.newcell()

    state_game2(AI_one, AI_two)
    Stop_versus = True
    y = random.choice(AI_two.directions)
    x0 = random.choice(AI_two.directions)
    x_adj = random.choice([AI_two.directions[AI_two.directions.index(x0) - 3], AI_two.directions[AI_two.directions.index(x0) - 1]])
    y = x_adj



    while(AI_one.status or AI_two.status):


        if y == x_adj:
                y = x0
        else: y = x_adj
        grid_test = AI_two.grid
        
        x = random.choice(directions)
        grid_test = AI_one.grid
        grid_test = AI_two.grid

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
        
        
        if AI_one.status and AI_one.grid != grid_test:
            AI_one.newcell()
        if AI_two.status and AI_one.grid != grid_test:
            AI_two.newcell()
        if skip is False:
            time.sleep(0.1)
            print(y)
            state_game2(AI_one,AI_two)
            
            state_game2(AI_one,AI_two)
    if(AI_one.score < AI_two.score):
        print(f"AI_two win this game, {strategie2} strategie won this time")
    else:
        print(f"AI_one win this game, {strategie1} strategie won this time")
    if AI_one.score > 730:
        average1 = ", lucky score !"
    if AI_two.score > 730:
        average2 = ", lucky score !"

    print(f"The final score for AI_one is {AI_one.score}{average1}")
    print(f"The final score is AI_two is {AI_two.score}{average2}")






Versus3(skip=False)