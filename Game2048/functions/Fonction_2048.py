import random

# %% Grid creation, cells addition

def sup_2048(grid):
    """ Counts the amount of cells with values greater or equal than to 2048.

    :returns: the count of these cells.
    :rtype: int
    """

    count = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 2048:
                count += 1
    return count


def newcell(grid):
    """ 
    Add new cell to the grid :

    - a 2 cell with 9/10 probability

    - a 4 cell with 1/10 probability

    See example:

        +---+---+---+---+
        | 0 | 2 | 2 | 0 |
        +---+---+---+---+
        | 0 | 0 | 0 | 0 |
        +---+---+---+---+
        | 0 | 0 | 0 | 0 |
        +---+---+---+---+
        | 0 | 0 | 0 | 0 |
        +---+---+---+---+

        becomes :

        +---+---+---+---+
        | 0 | 2 | 2 | 0 |
        +---+---+---+---+
        | 0 | 0 | 0 | 0 |
        +---+---+---+---+
        | 4 | 0 | 0 | 0 |
        +---+---+---+---+
        | 0 | 0 | 0 | 0 |
        +---+---+---+---+

    :returns: the new grid.
    """

    empty_cell = []  # Counts the number of empty cells and list them
    new_cell = 2
    pos = (0, 0)  # position on the grid
    for i in range(4):
        for j in range(4):
            if (grid[i][j] == 0):
                empty_cell.append((i, j))
    if random.uniform(a=0, b=1) > 0.90:  # Calculate the probability to add a 4 cell
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
    """ 
    Initializes the grid with :

    - a 2 cell with 9/10 probability

    - a 4 cell with 1/10 probability

    :returns: the initialized grid
    """

    new_cell = 2
    pos1 = random.randint(a=0, b=3)
    pos2 = random.randint(a=0, b=3)
    if random.uniform(a=0, b=1) > 0.90:
        new_cell = 4
    grid[pos1][pos2] = new_cell


def new_game():
    """
    Sets the start of the game (create the grid and add two random cells)
    """

    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    newcell_start(new_grid)
    newcell(new_grid)
    # score = 0
    return(new_grid)


def possible_action(grid):
    """ 
    Checks if a movement is possible on the grid.

    See example:

        In this grid, cells [0][0] and [0][1] can be merged in up and down movements.

        +---+---+---+---+
        | 2 | 4 | 8 | 4 |
        +---+---+---+---+
        | 2 | 8 | 4 | 8 |
        +---+---+---+---+
        | 4 | 2 | 8 | 4 |
        +---+---+---+---+
        | 2 | 4 | 2 | 8 |
        +---+---+---+---+

        Whereas in this one, no cells can be merged.

        +---+---+---+---+
        | 8 | 4 | 8 | 4 |
        +---+---+---+---+
        | 2 | 8 | 4 | 8 |
        +---+---+---+---+
        | 4 | 2 | 8 | 4 |
        +---+---+---+---+
        | 2 | 4 | 2 | 8 |
        +---+---+---+---+

    :returns: True if the movement is possible, false otherwise.
    :rtype: bool
    """

    p_a = False
    for i in range(3):
        for j in range(3):
            if (grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j+1]):
                p_a = True

    for j in range(3):
        if (grid[3][j] == grid[3][j+1]):
            p_a = True

    for i in range(3):
        if (grid[i][3] == grid[i+1][3]):
            p_a = True

    return p_a


def stop_game(grid):
    """ Checks if the game should be stop (when there is no more possible movement).

    :returns: True if the game can continued, false otherwise.
    :rtype: bool
    """

    full_cell = 0
    game_over = True
    for i in range(4):
        for j in range(4):
            if (grid[i][j] != 0):
                full_cell += 1
    if (full_cell == 16 and not possible_action(grid)):
        game_over = False
    return(game_over)


def state_game(grid, score):
    """
    Displays the grid and score in a terminal.

    See example :

        +---------------------+
        |  +---+---+---+---+  |
        |  | 0 | 2 | 2 | 4 |  |
        |  +---+---+---+---+  |
        |  | 0 | 0 | 4 | 2 |  |
        |  +---+---+---+---+  |
        |  | 4 | 0 | 2 | 2 |  |
        |  +---+---+---+---+  |
        |  | 8 | 2 | 4 | 8 |  |
        |  +---+---+---+---+  |
        +---------------------+
        |  Your score is 32   |
        +---------------------+

    """

    print(grid[0], '\n', grid[1], '\n', grid[2], '\n',
          grid[3], '\n', f'Your score is {score}')
    # print(grid[1])
    # print(grid[2])
    # print(grid[3])
    # print(f"Your score is {score}")
    return('------------')


# Step 1 : game creation
# Step 2 : new cell
# Step 3 : movement
# Step 4 : game state
# %% Cells movement
# Useful functions: stack, merge

aaa = [[1, 0, 0, 2], [0, 0, 3, 2], [0, 4, 0, 0], [1, 2, 0, 2]]

def stack(grid):
    """ Stacks the grid's cells to the left.

    See example:

        +---+---+---+---+
        | 0 | 2 | 0 | 2 |
        +---+---+---+---+
        | 0 | 0 | 0 | 8 |
        +---+---+---+---+
        | 4 | 0 | 0 | 2 |
        +---+---+---+---+
        | 0 | 2 | 8 | 0 |
        +---+---+---+---+

        becomes :

        +---+---+---+---+
        | 2 | 2 | 0 | 0 |
        +---+---+---+---+
        | 8 | 0 | 0 | 0 |
        +---+---+---+---+
        | 4 | 2 | 0 | 0 |
        +---+---+---+---+
        | 2 | 8 | 0 | 0 |
        +---+---+---+---+
        """

    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        position = 0
        for j in range(4):
            if (grid[i][j] != 0):
                new_grid[i][position] = grid[i][j]
                position += 1
    return new_grid


def merge_left(grid, score):
        """ Merges the grid cells to the left.

        See example:

            +---+---+---+---+
            | 0 | 2 | 2 | 0 |
            +---+---+---+---+
            | 2 | 4 | 4 | 2 |
            +---+---+---+---+
            | 0 | 2 | 0 | 4 |
            +---+---+---+---+
            | 8 | 8 | 8 | 8 |
            +---+---+---+---+

            becomes :

            +----+----+----+----+
            |  0 |  4 |  0 |  0 |
            +----+----+----+----+
            |  0 |  8 |  0 |  2 |
            +----+----+----+----+
            |  0 |  2 |  0 |  4 |
            +----+----+----+----+
            | 16 |  0 | 16 |  0 |
            +----+----+----+----+
        """

        for i in range(4):
            for j in range(3):
                if(grid[i][j] == grid[i][j+1]):
                    grid[i][j] = grid[i][j] * 2
                    grid[i][j + 1] = 0
                    score += grid[i][j]
        return (grid, score)




#  Rotation functions

def rotation(grid):
    """ 
    Rotate the grid according to an axial symmetry.
    It will be used to define movements.
    All movements are based on :py:func:`merge_left` and left :py:func:`left stack`.

    See example:

        +---+---+---+---+
        | 2 | 2 | 2 | 2 |
        +---+---+---+---+
        | 0 | 2 | 2 | 2 |
        +---+---+---+---+
        | 0 | 0 | 2 | 2 |
        +---+---+---+---+
        | 0 | 0 | 0 | 2 |
        +---+---+---+---+

        becomes :

        +---+---+---+---+
        | 2 | 2 | 2 | 2 |
        +---+---+---+---+
        | 2 | 2 | 2 | 0 |
        +---+---+---+---+
        | 2 | 2 | 0 | 0 |
        +---+---+---+---+
        | 2 | 0 | 0 | 0 |
        +---+---+---+---+
    """

    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[i][3-j]
    return new_grid


def transpose(grid):
    """ 
    Transposes (mathematically) the grid. It will be used to define movements.
    All movements are based on :py:func:`merge_left` and left :py:func:`left stack`.

    See example:

        +---+---+---+---+
        | 2 | 2 | 2 | 2 |
        +---+---+---+---+
        | 0 | 2 | 2 | 2 |
        +---+---+---+---+
        | 0 | 0 | 2 | 2 |
        +---+---+---+---+
        | 0 | 0 | 0 | 2 |
        +---+---+---+---+

        becomes :

        +---+---+---+---+
        | 2 | 0 | 0 | 0 |
        +---+---+---+---+
        | 2 | 2 | 0 | 0 |
        +---+---+---+---+
        | 2 | 2 | 2 | 0 |
        +---+---+---+---+
        | 2 | 2 | 2 | 2 |
        +---+---+---+---+

    :returns: the transposed grid.
    """
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        for j in range(4):
            new_grid[j][i] = grid[i][j]
    return new_grid


def inverse(grid):
    """ 
    Rotate the grid according to an axial symmetry.
    It will be used to define movements.
    All movements are based on :py:func:`merge_left` and left :py:func:`left stack`.

    See example:

        +---+---+---+---+
        | 2 | 2 | 2 | 2 |
        +---+---+---+---+
        | 0 | 2 | 2 | 2 |
        +---+---+---+---+
        | 0 | 0 | 2 | 2 |
        +---+---+---+---+
        | 0 | 0 | 0 | 2 |
        +---+---+---+---+

        becomes :

        +---+---+---+---+
        | 2 | 2 | 2 | 2 |
        +---+---+---+---+
        | 2 | 2 | 2 | 0 |
        +---+---+---+---+
        | 2 | 2 | 0 | 0 |
        +---+---+---+---+
        | 2 | 0 | 0 | 0 |
        +---+---+---+---+
    """
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[i][3-j]
    return new_grid

# All movement are base on rotation and
# left_movement (algorithms can be optimized)

def left_movement(grid, score):
    """ 
    Makes the complete move of the cells to the left.

    See example:

        +---+---+---+---+
        | 2 | 2 | 0 | 0 |
        +---+---+---+---+
        | 0 | 0 | 2 | 2 |
        +---+---+---+---+
        | 0 | 0 | 0 | 2 |
        +---+---+---+---+
        | 4 | 4 | 0 | 2 |
        +---+---+---+---+

        becomes :

        +---+---+---+---+
        | 4 | 0 | 0 | 0 |
        +---+---+---+---+
        | 4 | 0 | 0 | 0 |
        +---+---+---+---+
        | 2 | 0 | 0 | 0 |
        +---+---+---+---+
        | 8 | 2 | 0 | 0 |
        +---+---+---+---+

    :returns: the grid and the score after completing a left movement.
    """

    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    new_grid = stack(grid)
    new_grid, score = merge_left(new_grid, score)
    new_grid = stack(new_grid)
    return new_grid, score


def up_movement(grid, score):
    """ 
    Makes the complete move of the cells to the top.

    See example:

        +---+---+---+---+
        | 2 | 2 | 0 | 0 |
        +---+---+---+---+
        | 0 | 0 | 2 | 2 |
        +---+---+---+---+
        | 0 | 0 | 0 | 2 |
        +---+---+---+---+
        | 4 | 4 | 0 | 2 |
        +---+---+---+---+

        becomes :

        +---+---+---+---+
        | 2 | 2 | 2 | 4 |
        +---+---+---+---+
        | 4 | 4 | 0 | 2 |
        +---+---+---+---+
        | 0 | 0 | 0 | 0 |
        +---+---+---+---+
        | 0 | 0 | 0 | 0 |
        +---+---+---+---+

    :returns: the grid and the score after completing an up movement.
    """
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    new_grid = transpose(grid)
    new_grid = stack(new_grid)
    new_grid, score = merge_left(new_grid, score)
    new_grid = stack(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, score


def down_movement(grid, score):
    """ 
    Makes the complete move of the cells to the bottom.

    See example:

        +---+---+---+---+
        | 2 | 2 | 0 | 0 |
        +---+---+---+---+
        | 0 | 0 | 2 | 2 |
        +---+---+---+---+
        | 0 | 0 | 0 | 2 |
        +---+---+---+---+
        | 4 | 4 | 0 | 2 |
        +---+---+---+---+

        becomes :

        +---+---+---+---+
        | 0 | 0 | 0 | 0 |
        +---+---+---+---+
        | 0 | 0 | 0 | 0 |
        +---+---+---+---+
        | 2 | 2 | 0 | 2 |
        +---+---+---+---+
        | 4 | 4 | 2 | 4 |
        +---+---+---+---+

    :returns: the grid and the score after completing an up movement.
    """

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
    """ 
    Makes the complete move of the cells to the right.

    See example:

        +---+---+---+---+
        | 2 | 2 | 0 | 0 |
        +---+---+---+---+
        | 0 | 0 | 2 | 2 |
        +---+---+---+---+
        | 0 | 0 | 0 | 2 |
        +---+---+---+---+
        | 4 | 4 | 0 | 2 |
        +---+---+---+---+

        becomes :

        +---+---+---+---+
        | 0 | 0 | 0 | 4 |
        +---+---+---+---+
        | 0 | 0 | 0 | 4 |
        +---+---+---+---+
        | 0 | 0 | 0 | 2 |
        +---+---+---+---+
        | 0 | 0 | 8 | 2 |
        +---+---+---+---+

    :returns: the grid and the score after completing an up movement.
    """
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    new_grid = rotation(grid)
    new_grid, score = left_movement(new_grid, score)
    new_grid = rotation(new_grid)
    return new_grid, score
