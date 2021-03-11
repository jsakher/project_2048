# %% Test

# Color and dictionary creation

index_cell = []

for i in range(1, 18):
    index_cell.append(2**i)

color_cell1 = ['#fef198', '#f5e28f', '#ebd385', '#e1c47c', '#d7b672',
               '#cda869', '#c49a60', '#ba8c56', '#b07e4d', '#a77044',
               '#9d623b', '#935532', '#8a4729', '#803920',
               '#772a17', '#6e190c', '#650000']

cell1 = zip(index_cell, color_cell1)



aaa = [[0, 2, 0, 4], [0, 0, 0, 2], [0, 0, 2, 2], [2, 2, 2, 2]]


# %% Mouvement de la grille
#  Utility functions: stack, merge,
aaa = [[0, 2, 0, 4], [0, 0, 0, 2], [0, 0, 2, 2], [2, 2, 2, 2]]

def  stack(grid):

    """  Stack the grid  """

    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    for i in range(4):
        position = 0
        for j in range(4):
            if (grid[i][j] != 0):
                new_grid[i][position] = grid[i][j]
                position += 1
    return new_grid


def  merge_left(grid):

    """  merge the grid on the left  """

    for i in range(4): 
        for j in range(3):
            if(grid[i][j] == grid[i][j+1] and grid[i][j] != 0):
                grid[i][j] = grid[i][j] * 2
                grid[i][j + 1] = 0
    return grid

#  Rotation functions

def  rotation(grid):
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[i][3-j]
    return new_grid


def  rotationantih(grid):
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    new_grid = rotation(grid)

    new_grid = list(zip(*new_grid))
    return new_grid


def  rotationh(grid):
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    for i in range(4):
        
        for j in range(4):
            new_grid[i][j] = grid[3-i][j]

    new_grid = list(zip(*new_grid))
    return new_grid

# All movement are base on rotation and left_movement (On peut optimiser les algo)
def  left_movement(grid):

    """ moove grid to the left"""

    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    new_grid = stack(grid)
    new_grid = merge_left(new_grid)
    new_grid = stack(new_grid)
    return new_grid


def up_movement(grid):
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    new_grid = rotationantih(grid)
    new_grid = stack(new_grid)
    new_grid = merge_left(new_grid)
    new_grid = stack(new_grid)
    new_grid = rotationantih(new_grid)
    new_grid = rotationantih(new_grid)
    new_grid = rotationantih(new_grid)
    return new_grid


def down_movement(grid):

    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    new_grid = rotationh(grid)
    new_grid = stack(new_grid)
    new_grid = merge_left(new_grid)
    new_grid = stack(new_grid)
    new_grid = rotationantih(new_grid)
    return new_grid


def  right_movement(grid):
    """ moove grid to the right"""
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    new_grid = rotation(grid) 
    new_grid = left_movement(new_grid) 
    new_grid = rotation(new_grid) 
    return new_grid


print(aaa)
print(up_movement(aaa))
# %%
