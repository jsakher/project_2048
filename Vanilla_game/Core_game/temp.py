import Main



# %% Function 

# Color and dictionary creation (visualisation pour plus tard)

index_cell = []

for i in range(1, 18):
    index_cell.append(2**i)

color_cell1 = ['#fef198', '#f5e28f', '#ebd385', '#e1c47c', '#d7b672',
               '#cda869', '#c49a60', '#ba8c56', '#b07e4d', '#a77044',
               '#9d623b', '#935532', '#8a4729', '#803920',
               '#772a17', '#6e190c', '#650000']

cell1 = zip(index_cell, color_cell1)


# %% Création de la grille, ajout des cellules (gestion aléatoire)
import random

def newcell(grid):
    ''' Add new cell on the grid with probabily 9/10 add a 2 and 1/10 add a 4 '''

    empty_cell = [] # Count the number of empty cell and list them
    new_cell = 2 
    pos = (0, 0) # position on the grid
    for i in range(4):
        for j in range(4):
            if (grid[i][j] == 0):
                empty_cell.append((i, j)) 
    if random.uniform(a=0, b=1) > 0.90: # Calculate the probability to add a 4
        new_cell = 4
    todo = len(empty_cell) 
    if todo == 0:
        todo +=1
    pos = random.randint(a=0, b=todo-1) # Calculate how to add the new cell
    if len(empty_cell) == 0:
        pos = [0, 0]
    else :
        pos = empty_cell[pos]
    a, b = pos[0], pos[1]
    grid[a][b] = new_cell

    return grid

    
def newcell_start(grid):
    ''' Add new cell on the empty grid with probabily 9/10 add a 2 and 1/10 add a 4 '''

    new_cell = 2 
    pos1 = random.randint(a=0, b=3)
    pos2 = random.randint(a=0, b=3)
    if random.uniform(a=0, b=1) > 0.90:
        new_cell = 4
    grid[pos1][pos2] = new_cell

def new_game():
    ''' Set the start of the game, create the grid and add two random cell '''

    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    newcell_start(new_grid)
    newcell(new_grid)
    #score = 0
    return(new_grid)

def stop_game(grid): #Game stops when there is no possible movement to make (i.e. cannot merge any cells), not when the grid is full !
    ''' Check every step if you lose '''

    full_cell = 0
    game_over = True
    for i in range(4):
        for j in range(4):
            if (grid[i][j] != 0):
                full_cell += 1
    if full_cell == 16:
        game_over = False
    return(game_over)

def state_game(grid, score):
    ''' Display the grid's state '''

    print(grid[0])
    print(grid[1])
    print(grid[2])
    print(grid[3])
    print(f"Your score is {score}")
    return('------------')


# Etape 1 cration du jeu etape 2 nouvelle cell 3 mouvement 4 etat du jeu if false on continue etc....
# %% Mouvement de la grille
#  Utility functions: stack, merge,
aaa = [[1, 0, 0, 2], [0, 0, 3, 2], [0, 4, 0, 0], [1, 2, 0, 2]]

def  stack(grid):
    ''' Stack the grid on the left side '''

    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        position = 0
        for j in range(4):
            if (grid[i][j] != 0):
                new_grid[i][position] = grid[i][j]
                position += 1
    return new_grid


def  merge_left(grid, score):
    ''' Merge the grid on the left  '''
    #reward = 0
    for i in range(4): 
        for j in range(3):
            if(grid[i][j] == grid[i][j+1]): # revoir ; A:"range(n) renvoie les n premiers integers en partant de 0 => range(3) contient les 3 premiers chiffres en partant de 0 " 
                grid[i][j] = grid[i][j] * 2 # Aucune modification à faire donc.
                grid[i][j + 1] = 0
                score += grid[i][j]
    return (grid, score) 

#  Rotations functions

def  rotation(grid):
    ''' Rotate the grid, usefull to make movement'''

    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[i][3-j]
    return new_grid


def transpose(grid):
    ''' Transpose the grid, usefull to make movement '''
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
    for i in range(4): 
        for j in range(4): 
            new_grid[j][i] = grid[i][j]
    return new_grid


def inverse(grid):
    ''' inverse the grid, usefull to make movement ''' 
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
    for i in range(4): 
        for j in range(4): 
            new_grid[i][j] = grid[i][3-j]
    return new_grid

# All movement are base on rotation and left_movement (On peut optimiser les algo)

def  left_movement(grid, score):
    ''' Move grid to the left '''

    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    new_grid = stack(grid)
    new_grid, score = merge_left(new_grid, score)
    new_grid = stack(new_grid)
    return new_grid, score


def up_movement(grid, score):
    ''' Move grid to the top '''
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    new_grid = transpose(grid)
    new_grid = stack(new_grid)
    new_grid, score = merge_left(new_grid, score)
    new_grid = stack(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, score



def down_movement(grid, score):
    ''' Move grid to the botom '''
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    new_grid = transpose(grid)
    new_grid = inverse(new_grid)
    new_grid = stack(new_grid)
    new_grid, score = merge_left(new_grid, score)
    new_grid = stack(new_grid)
    new_grid = inverse(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, score


def  right_movement(grid, score):
    ''' Move grid to the left '''
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    new_grid = rotation(grid) 
    new_grid, score = left_movement(new_grid, score) 
    new_grid = rotation(new_grid) 
    return new_grid, score



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

    AI_one.newcell_start()
    AI_one.newcell()

    AI_two.newcell_start()
    AI_two.newcell()
    state_game2(AI_one, AI_two)
    Stop_versus = True

    while(AI_one.status or AI_two.status):
        time.sleep(1)
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

Versus('random', 'random', False)