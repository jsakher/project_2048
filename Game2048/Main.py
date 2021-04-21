""" Write down a short description of what this module is composed. """

import random
import time

class Game_2048():
    """ Contains the necessary functions to  launch either the 2048 user game or the A.I. ones.

    """

    def __init__(self):
        """ The constructor. """
        self.grid = [[0, 0, 0, 0], [0, 0, 0, 0],
                     [0, 0, 0, 0], [0, 0, 0, 0]]
        self.score = 0
        self.status = True
        self.maxcell = 0
        self.goal = 0
        self.directions = ['z', 'q', 's', 'd']

    def maxcell_find(self):
        """ Identifies the greater value of the grid's cells. 

        :returns: the value of the identified cell.
        :rtype: int
        """
        check = 0
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] > check:
                    check = self.grid[i][j]
        self.maxcell = check
        return self.maxcell

    def sup_2048(self):
        """ Counts the amount of cells with values greater or equal than to 2048.
        
        :returns: the count of these cells.
        :rtype: int
        """
        count = 0
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] >= 2048:
                    count += 1
        self.goal = count
        return self.goal
    
    def newcell_start(self):
        """ Initializes the grid with :

        - a 2 cell with 9/10 probability

        - a 4 cell with 1/10 probability

        :returns: the initialized grid
        """

        new_cell = 2
        pos1 = random.randint(a=0, b=3)
        pos2 = random.randint(a=0, b=3)
        if random.uniform(a=0, b=1) > 0.90:
            new_cell = 4
        self.grid[pos1][pos2] = new_cell
        return self.grid

    def newcell(self):
        """ Add new cell to the grid :

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

        empty_cell = []
        new_cell = 2
        pos = (0, 0)
        for i in range(4):
            for j in range(4):
                if (self.grid[i][j] == 0):
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
        self.grid[a][b] = new_cell

        return self.grid

    def display(self):
        """ Displays the grid and score in a terminal.

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

        print(self.grid[0], '\n', self.grid[1], '\n', self.grid[2], '\n', self.grid[3], '\n', f'Your score is {self.score}')
        # print(self.grid[1])
        # print(self.grid[2])
        # print(self.grid[3])
        # print(f'Your score is {self.score}')

    def possible_action(self):
        """ Checks if a movement is possible on the grid.

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
                if(self.grid[i][j] == self.grid[i + 1][j] or self.grid[i][j] == self.grid[i][j + 1]):
                    p_a = True

        for j in range(3):
            if(self.grid[3][j] == self.grid[3][j + 1]):
                p_a = True

        for i in range(3):
            if(self.grid[i][3] == self.grid[i + 1][3]):
                p_a = True
        return p_a


    def stop_game(self):
        """ Checks if the game should be stop (when there is no more possible movement).
        
        :returns: True if the game can continued, false otherwise.
        :rtype: bool
        """

        full_cell = 0
        for i in range(4):
            for j in range(4):
                if (self.grid[i][j] != 0):
                    full_cell += 1
        if (full_cell == 16 and not self.possible_action()):
            self.status = False
        return self.status

    def stack(self):
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
                if (self.grid[i][j] != 0):
                    new_grid[i][position] = self.grid[i][j]
                    position += 1
        self.grid = new_grid
        return self.grid

    def merge_left(self):
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
                if(self.grid[i][j] == self.grid[i][j+1]):
                    self.grid[i][j] = self.grid[i][j] * 2
                    self.grid[i][j + 1] = 0
                    self.score += self.grid[i][j]
        return self.grid, self.score

    def transpose(self):
        """ Transposes (mathematically) the grid. It will be used to define movements.
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
                new_grid[j][i] = self.grid[i][j]
        self.grid = new_grid
        return self.grid

    def inverse(self):
        """ Rotate the grid according to an axial symmetry. It will be used to define movements.

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
                new_grid[i][j] = self.grid[i][3-j]
        self.grid = new_grid
        return self.grid

    def left_movement(self):
        """ Makes the complete move of the cells to the left.

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

        self.stack()
        self.merge_left()
        self.stack()
        return self.grid, self.score

    def up_movement(self):
        """ Makes the complete move of the cells to the top.

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

        self.transpose()
        self.stack()
        self.merge_left()
        self.stack()
        self.transpose()
        return self.grid, self.score

    def down_movement(self):
        """ Makes the complete move of the cells to the bottom.

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

        self.transpose()
        self.inverse()
        self.stack()
        self.merge_left()
        self.stack()
        self.inverse()
        self.transpose()
        return self.grid, self.score

    def right_movement(self):
        """ Makes the complete move of the cells to the right.

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

        self.inverse()
        self.left_movement()
        self.inverse()
        return self.grid, self.score

    def main(self):
        """ Launches the user game.

        Classic commands are used to play (azerty keyboard) :

        - z : up

        - q : left

        - d : right

        - s : down

        To do an action you must select a direction and  press enter.

        To quit, write "quit" and press enter.
        """
        self.newcell_start()
        self.newcell()
        self.display()

        while(self.status):

            x = input('press command')
            grid_test = self.grid

            if (x.upper() == 'D'):
                self.right_movement()
            if (x.upper() == 'Z'):
                self.up_movement()
            if (x.upper() == 'S'):
                self.down_movement()
            if (x.upper() == 'Q'):
                self.left_movement()
            if (x.upper() == 'QUIT'):
                self.status = False
            self.sup_2048()
            self.stop_game()
            if self.status and self.grid != grid_test :
                self.newcell()
            self.display()
            
            if self.status is False:
                if self.goal >= 1:
                    print(f'Game over, you win ! {self.goal} created.\n Your score is {self.score}')
                else:
                    print(f'Game over, you lose ! Your score is {self.score}')
                if self.score > 730: #  empirical mean see Algo_play
                    print(f'you did better than random IA')
                else:
                    print(f'you did worse than random IA')


    def demo(self, speed=0.4):
        """ Demo of an AI game (displayed)

        """
        directions = ['z', 'q', 's', 'd']
        self.newcell_start()
        self.newcell()
        self.display()
        scoring_step = []
        while(self.status):
            # time.sleep(speed)
            x = random.choice(directions)
            grid_test = self.grid

            if (x.upper() == 'D'):
                self.right_movement()
            if (x.upper() == 'Z'):
                self.up_movement()
            if (x.upper() == 'S'):
                self.down_movement()
            if (x.upper() == 'Q'):
                self.left_movement()
            if (x.upper() == 'QUIT'):
                self.status = False
            scoring_step.append(self.score)
            self.stop_game()
            if self.status and self.grid != grid_test:
                self.newcell()
            self.display()
            print(f'IA  play {x} movement')
            if self.status is False:
                print(f'IA lost is score is {self.score}')
        return scoring_step
    
    
    
    def random_2048(self):
        """ Launches an AI game with random movements only.
        """

        self.newcell_start()
        self.newcell()
        
        while(self.status):
            
            x = random.choice(self.directions)
            grid_test = self.grid

            if (x.upper() == 'D'):
                self.right_movement()
            if (x.upper() == 'Z'):
                self.up_movement()
            if (x.upper() == 'S'):
                self.down_movement()
            if (x.upper() == 'Q'):
                self.left_movement()
            self.stop_game()
            if self.status and self.grid != grid_test:
                self.newcell()
    
    def clockwise_2048(self):
        """ Launches an AI game with clockwise movement (starting movement is randomized).
        """
        self.newcell_start()
        self.newcell()
        x = random.choice(self.directions)
        #count = 0
        while(self.status):
            
            x = self.directions[self.directions.index(x) - 1]
            grid_test = self.grid

            if (x.upper() == 'D'):
                self.right_movement()
            if (x.upper() == 'Z'):
                self.up_movement()
            if (x.upper() == 'S'):
                self.down_movement()
            if (x.upper() == 'Q'):
                self.left_movement()
            self.stop_game()
            if self.status and self.grid != grid_test:
                self.newcell()
            #count = (count + 1) % 4

    def opposite_2048(self):
        """ Launches an AI game with only a first random movement and its opposite one.
        """
        
        self.newcell_start()
        self.newcell()
        x = random.choice(self.directions)
        block_game = 0

        while(self.status):
            
            x = self.directions[self.directions.index(x) - 2]
            grid_test = self.grid

            if (x.upper() == 'D'):
                self.right_movement()
            if (x.upper() == 'Z'):
                self.up_movement()
            if (x.upper() == 'S'):
                self.down_movement()
            if (x.upper() == 'Q'):
                self.left_movement()
            self.stop_game()
            if self.grid == grid_test:
                block_game += 1
            if self.status and self.grid != grid_test:
                self.newcell()
            if block_game > 3:
                self.status = False
            
            
            
            

    def adjacent_2048(self):
        """ Launches an AI game with only a first random movement and one of its adjacent ones.
        """
        
        self.newcell_start()
        self.newcell()
        x = random.choice(self.directions)
        x0 = random.choice(self.directions)
        x_adj = random.choice([self.directions[self.directions.index(x0) - 3], self.directions[self.directions.index(x0) - 1]])
        x = x_adj
        block_game = 0

        while(self.status):
            
            if x == x_adj:
                x = x0
            else: x = x_adj
            grid_test = self.grid

            if (x.upper() == 'D'):
                self.right_movement()
            if (x.upper() == 'Z'):
                self.up_movement()
            if (x.upper() == 'S'):
                self.down_movement()
            if (x.upper() == 'Q'):
                self.left_movement()
            self.stop_game()
            if self.grid == grid_test:
                block_game += 1
            if self.status and self.grid != grid_test:
                self.newcell()
            if block_game > 3:
                self.status = False

# Launch_game = Game()
# print('Command : z => up')
# print('Command : q => left')
# print('Command : d => right')
# print('Command : s => down')
# print('to do an action you must select a direction and  press enter')
# Launch_game.main() # Launch game


class Game_6561():
    """ Alternative game to 2048 with a 3x3 grid and a goal score of 6561.
    
    Contains the same functions as class :py:class:`Game_2048` (excepting A.I. plays ones).
    """

    def __init__(self):

        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.score = 0
        self.status = True

    def newcell_start(self):

        new_cell = 3
        pos1 = random.randint(a=0, b=2)
        pos2 = random.randint(a=0, b=2)
        if random.uniform(a=0, b=1) > 0.90:
            new_cell = 6
        self.grid[pos1][pos2] = new_cell
        return self.grid

    def newcell(self):

        empty_cell = []
        new_cell = 3
        pos = (0, 0)
        for i in range(3):
            for j in range(3):
                if (self.grid[i][j] == 0):
                    empty_cell.append((i, j))
        if random.uniform(a=0, b=1) > 0.90:
            new_cell = 6
        todo = len(empty_cell)
        if todo == 0:
            todo += 1
        pos = random.randint(a=0, b=todo-1)
        if len(empty_cell) == 0:
            pos = [0, 0]
        else:
            pos = empty_cell[pos]
        a, b = pos[0], pos[1]
        self.grid[a][b] = new_cell

        return self.grid

    def display(self):

        print(self.grid[0])
        print(self.grid[1])
        print(self.grid[2])
        print(f'Your score is {self.score}')

    def possible_action(self):

        p_a = False
        for i in range(2):
            for j in range(2):
                if(self.grid[i][j] == self.grid[i + 1][j] or self.grid[i][j] == self.grid[i][j + 1]):
                    p_a = True

        for j in range(2):
            if(self.grid[2][j] == self.grid[2][j + 1]):
                p_a = True

        for i in range(2):
            if(self.grid[i][2] == self.grid[i + 1][2]):
                p_a = True
        return p_a


    def stop_game(self):

        full_cell = 0
        for i in range(3):
            for j in range(3):
                if (self.grid[i][j] != 0):
                    full_cell += 1
        if (full_cell == 9 and not self.possible_action()):
            self.status = False
        return self.status

    def stack(self):

        new_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            position = 0
            for j in range(3):
                if (self.grid[i][j] != 0):
                    new_grid[i][position] = self.grid[i][j]
                    position += 1
        self.grid = new_grid
        return self.grid

    def merge_left(self):
 
        for i in range(3):
            for j in range(2):
                if(self.grid[i][j] == self.grid[i][j+1]):
                    self.grid[i][j] = self.grid[i][j] * 3
                    self.grid[i][j + 1] = 0
                    self.score += self.grid[i][j]
        return self.grid, self.score

    def transpose(self):

        new_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                new_grid[j][i] = self.grid[i][j]
        self.grid = new_grid
        return self.grid

    def inverse(self):

        new_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                new_grid[i][j] = self.grid[i][2-j]
        self.grid = new_grid
        return self.grid

    def left_movement(self):

        self.stack()
        self.merge_left()
        self.stack()
        return self.grid, self.score

    def up_movement(self):
        
        self.transpose()
        self.stack()
        self.merge_left()
        self.stack()
        self.transpose()
        return self.grid, self.score

    def down_movement(self):

        self.transpose()
        self.inverse()
        self.stack()
        self.merge_left()
        self.stack()
        self.inverse()
        self.transpose()
        return self.grid, self.score

    def right_movement(self):

        self.inverse()
        self.left_movement()
        self.inverse()
        return self.grid, self.score

    def main(self):

        self.newcell_start()
        self.newcell()
        self.display()

        while(self.status):

            x = input('press command')
            grid_test = self.grid

            if (x.upper() == 'D'):
                self.right_movement()
            if (x.upper() == 'Z'):
                self.up_movement()
            if (x.upper() == 'S'):
                self.down_movement()
            if (x.upper() == 'Q'):
                self.left_movement()
            if (x.upper() == 'QUIT'):
                self.status = False
            self.stop_game()
            if self.status and self.grid != grid_test:
                self.newcell()
            self.display()
            if self.status is False:
                print(f'you lose your score is {self.score}')

    def demo(self):

        self.newcell_start()
        self.newcell()
        self.display()

        directions = ['z', 'q', 's', 'd']

        while(self.status):
            time.sleep(2)
            x = random.choice(directions)
            x = input('press command')
            grid_test = self.grid

            if (x.upper() == 'D'):
                self.right_movement()
            if (x.upper() == 'Z'):
                self.up_movement()
            if (x.upper() == 'S'):
                self.down_movement()
            if (x.upper() == 'Q'):
                self.left_movement()
            if (x.upper() == 'QUIT'):
                self.status = False
            self.stop_game()
            if self.status and self.grid != grid_test:
                self.newcell()
            self.display()
            if self.status is False:
                print(f'you lose your score is {self.score}')


