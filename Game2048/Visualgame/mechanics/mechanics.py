import random


class mechanics():
    def __init__(self):
        """ Create new grid """
        # self.grid = [[0, 0, 0, 0], [0, 0, 0, 0],
        #              [0, 0, 0, 0], [0, 0, 0, 0]]
        # self.score = 0
        # self.status = True
        # self.maxcell = 0
        # self.goal = 0

    @staticmethod
    def maxcell_find(grid):
        ''' Identifies the value of the maximum cell self.grid'''
        maxcell = 0
        for i in range(4):
            for j in range(4):
                if grid[i][j] > maxcell:
                    maxcell = grid[i][j]
        return maxcell

    @staticmethod
    def sup_2048(grid):
        ''' Counts the amount of cells with value 
        greater than or equal to 2048'''
        goal = 0
        for i in range(4):
            for j in range(4):
                if grid[i][j] >= 2048:
                    goal += 1
        return goal

    @staticmethod
    def newcell_start(grid):
        ''' Add new cell to the grid when grid is empty.
            Probability are 1/10 to be a 4
                            9/10 to be a 2

        see example:

            grid [0, 0, 0, 0]  Become  [0, 0, 2, 0]
                 [0, 0, 0, 0]          [0, 0, 0, 0]
                 [0, 0, 0, 0]          [0, 0, 0, 0]
                 [0, 0, 0, 0]          [0, 0, 0, 0]
        '''

        new_cell = 2
        pos1 = random.randint(a=0, b=3)
        pos2 = random.randint(a=0, b=3)
        if random.uniform(a=0, b=1) > 0.90:
            new_cell = 4
        grid[pos1][pos2] = new_cell
        return grid

    @staticmethod
    def newcell(grid):
        ''' Add new cell to the grid.
            Probability are  1/10 to be a 4
                             9/10 to be a 2

        see example:

            grid [0, 2, 2, 0]  Become  [0, 2, 2, 0]
                 [0, 0, 0, 0]          [0, 0, 0, 0]
                 [0, 0, 0, 0]          [4, 0, 0, 0]
                 [0, 0, 0, 0]          [0, 0, 0, 0]
        '''

        empty_cell = []
        new_cell = 2
        pos = (0, 0)
        for i in range(4):
            for j in range(4):
                if (grid[i][j] == 0):
                    empty_cell.append((i, j))
        if random.uniform(a=0, b=1) > 0.90:
            new_cell = 4
        todo = len(empty_cell)
        if todo == 0:
            todo += 1
        pos = random.randint(a=0, b=todo-1)
        if len(empty_cell) == 0:
            pos = [0, 0]
        else:
            pos = empty_cell[pos]
        a, b = pos[0], pos[1]
        grid[a][b] = new_cell

        return grid

    @staticmethod
    def display(grid, score):
        ''' Display grid and score.

        see example:
                [0, 2, 2, 4]
                [0, 0, 4, 2]
                [4, 0, 2, 2]
                [8, 2, 4, 8]
                Your score is 32
        '''

        print(grid[0])
        print(grid[1])
        print(grid[2])
        print(grid[3])
        print(f'Your score is {score}')

    @staticmethod
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
                if(grid[i][j] == grid[i + 1][j] or grid[i][j] == grid[i][j + 1]):
                    p_a = True

        for j in range(3):
            if(grid[3][j] == grid[3][j + 1]):
                p_a = True

        for i in range(3):
            if(grid[i][3] == grid[i + 1][3]):
                p_a = True
        return p_a

    @staticmethod
    def stop_game(grid, possible_action, status):
        ''' Check every step if you lose to stop
        the game when there is no possible movement
        '''

        full_cell = 0
        for i in range(4):
            for j in range(4):
                if (grid[i][j] != 0):
                    full_cell += 1
        if (full_cell == 16 and not possible_action()):
            status = False
        return status

    @staticmethod
    def stack(grid):
        ''' Stack the grid to the left.

        see example:

            grid [0, 2, 0, 2]  Become  [2, 2, 0, 0]
                 [0, 0, 0, 8]          [8, 0, 0, 0]
                 [4, 0, 0, 2]          [4, 2, 0, 0]
                 [0, 2, 8, 0]          [2, 8, 0, 0]
        '''

        new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(4):
            position = 0
            for j in range(4):
                if (grid[i][j] != 0):
                    new_grid[i][position] = grid[i][j]
                    position += 1
        grid = new_grid
        return grid

    @staticmethod
    def merge_left(grid, score):
        ''' Merge grid to the left.

        see example:

            grid = [0, 2, 2, 0]  Become [0, 4, 0, 0]
                   [2, 4, 4, 2]         [2, 8, 0, 2]
                   [0, 2, 0, 4]         [0, 2, 0, 4]
                   [8, 8, 8, 8]         [16, 0, 16, 0]

        '''

        for i in range(4):
            for j in range(3):
                if(grid[i][j] == grid[i][j+1]):
                    grid[i][j] = grid[i][j] * 2
                    grid[i][j + 1] = 0
                    score += grid[i][j]
        return grid, score

    @staticmethod
    def transpose(grid):
        ''' Transpose the grid, usefull to make movement.
        All movement are base on left merge, left stack

        see example:

            grid = [2, 2, 2, 2]  Become [2, 0, 0, 0]
                   [0, 2, 2, 2]         [2, 2, 0, 0]
                   [0, 0, 2, 2]         [2, 2, 2, 0]
                   [0, 0, 0, 2]         [2, 2, 2, 2]
        '''

        new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(4):
            for j in range(4):
                new_grid[j][i] = grid[i][j]
        grid = new_grid
        return grid

    @staticmethod
    def inverse(grid):
        ''' Inverse the grid, usefull to make movement.
        All movement are base on left merge, left stack

        see example:

            grid = [2, 2, 2, 2]  Become [2, 2, 2, 2]
                   [0, 2, 2, 2]         [2, 2, 2, 0]
                   [0, 0, 2, 2]         [2, 2, 0, 0]
                   [0, 0, 0, 2]         [2, 0, 0, 0]
        '''

        new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(4):
            for j in range(4):
                new_grid[i][j] = grid[i][3-j]
        grid = new_grid
        return grid


    def left_movement(self, grid, score):
        ''' Move grid to the left

        see example:

            grid = [2, 2, 0, 0]  Become [4, 0, 0, 0]
                   [0, 0, 2, 2]         [4, 0, 0, 0]
                   [0, 0, 0, 2]         [2, 0, 0, 0]
                   [4, 4, 0, 2]         [8, 2, 0, 0]
        '''

        grid = self.stack(grid)
        grid, score = self.merge_left(grid, score)
        grid = self.stack(grid)
        return grid, score

 
    def up_movement(self, grid, score):
        ''' Move grid to the top

        see example:

            grid = [2, 2, 0, 0]  Become [2, 2, 2, 4]
                   [0, 0, 2, 2]         [4, 4, 0, 2]
                   [0, 0, 0, 2]         [0, 0, 0, 0]
                   [4, 4, 0, 2]         [0, 0, 0, 0]
        '''

        grid = self.transpose(grid)
        grid = self.stack(grid)
        grid, score = self.merge_left(grid, score)
        grid = self.stack(grid)
        grid = self.transpose(grid)
        return grid, score


    def down_movement(self, grid, score):
        ''' Move grid to the bottom

        see example:

            grid = [2, 2, 0, 0]  Become [0, 0, 0, 0]
                   [0, 0, 2, 2]         [0, 0, 0, 0]
                   [0, 0, 0, 2]         [2, 2, 0, 2]
                   [4, 4, 0, 2]         [4, 4, 2, 4]
        '''

        grid = self.transpose(grid)
        grid = self.inverse(grid)
        grid = self.stack(grid)
        grid, score = self.merge_left(grid, score)
        grid = self.stack(grid)
        grid = self.inverse(grid)
        grid = self.transpose(grid)
        return grid, score


    def right_movement(self, grid, score):
        ''' Move grid to the right

        see example:

            grid = [2, 2, 0, 0]  Become [0, 0, 0, 4]
                   [0, 0, 2, 2]         [0, 0, 0, 4]
                   [0, 0, 0, 2]         [0, 0, 0, 2]
                   [4, 4, 0, 2]         [0, 0, 8, 2]
        '''

        grid = self.inverse(grid)
        grid, score = self.left_movement(grid, score)
        grid = self.inverse(grid)
        return grid, score
