# %% Function

import random

# %% Création de la grille, ajout des cellules (gestion aléatoire)

def sup_2048(grid):
    '''Counts the amount of cells with value 
        greater than or equal to 2048'''
    count = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 2048:
                count += 1
    return count

def newcell(grid):
    ''' Add new cell on the grid with probabily 9/10 add a 2 and 1/10 add a 4 '''

    empty_cell = []  # Count the number of empty cell and list them
    new_cell = 2
    pos = (0, 0)  # position on the grid
    for i in range(4):
        for j in range(4):
            if (grid[i][j] == 0):
                empty_cell.append((i, j))
    if random.uniform(a=0, b=1) > 0.90:  # Calculate the probability to add a 4
        new_cell = 4
    todo = len(empty_cell)
    if todo == 0:
        todo += 1
    pos = random.randint(a=0, b=todo-1)  # Calculate how to add the new cell
    if len(empty_cell) == 0:
        pos = [0, 0]
    else:
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


def possible_action(grid):
    '''Checks if a movement is possible on the grid
        
        See example:
         grid1 = [2, 4, 8, 4]                           grid2 = [8, 4, 8, 4]
                 [2, 8, 4, 8]                                   [2, 8, 4, 8]
                 [4, 2, 8, 4]                                   [4, 2, 8, 4]
                 [2, 4, 2, 8]                                   [2, 4, 2, 8]
         grid1[0][0] and grid1[1][0] can be merged.      No two cells can be merged.'''
    p_a = False
    for i in range(3):
        for j in range(3):
            if (grid[i][j] == grid[i+1][j] or grid[i][j] == grid [i][j+1]):
                p_a = True
        
    for j in range(3):
        if (grid[3][j] == grid[3][j+1]):
            p_a = True

    for i in range(3):
        if (grid[i][3] == grid[i+1][3]):
            p_a = True

    return p_a
        

def stop_game(grid):  # Game stops when there is no possible movement to make (i.e. cannot merge any cells), not when the grid is full !
    ''' Check every step if you lose '''

    full_cell = 0
    game_over = True
    for i in range(4):
        for j in range(4):
            if (grid[i][j] != 0):
                full_cell += 1
    if (full_cell == 16 and not possible_action(grid)) :
        game_over = False
    return(game_over)


def state_game(grid, score):
    ''' Display the grid's state '''

    print(grid[0], '\n', grid[1], '\n', grid[2], '\n', grid[3], '\n', f'Your score is {score}')
    # print(grid[1])
    # print(grid[2])
    # print(grid[3])
    # print(f"Your score is {score}")
    return('------------')


# Etape 1 cration du jeu etape 2 nouvelle cell 3 mouvement 4 etat du jeu if false on continue etc....
# %% Mouvement de la grille
#  Utility functions: stack, merge,
aaa = [[1, 0, 0, 2], [0, 0, 3, 2], [0, 4, 0, 0], [1, 2, 0, 2]]


def stack(grid):
    ''' Stack the grid on the left side '''

    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        position = 0
        for j in range(4):
            if (grid[i][j] != 0):
                new_grid[i][position] = grid[i][j]
                position += 1
    return new_grid


def merge_left(grid, score):
    ''' Merge the grid on the left  '''
    #reward = 0
    for i in range(4):
        for j in range(3):
            # revoir ; A:"range(n) renvoie les n premiers integers en partant de 0 => range(3) contient les 3 premiers chiffres en partant de 0 "
            if(grid[i][j] == grid[i][j+1]):
                # Aucune modification à faire donc.
                grid[i][j] = grid[i][j] * 2
                grid[i][j + 1] = 0
                score += grid[i][j]
    return (grid, score)

#  Rotations functions


def rotation(grid):
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


def left_movement(grid, score):
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


def right_movement(grid, score):
    ''' Move grid to the left '''
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    new_grid = rotation(grid)
    new_grid, score = left_movement(new_grid, score)
    new_grid = rotation(new_grid)
    return new_grid, score


# %%
