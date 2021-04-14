import random
import time
class Game_2048():
    """ This class represent gamegrid and function"""

    def __init__(self):
        """ Create new grid """
        self.grid = [[0, 0, 0, 0], [0, 0, 0, 0],
                     [0, 0, 0, 0], [0, 0, 0, 0]]
        self.score = 0
        self.status = True
        self.maxcell = 0
        self.goal = 0
        self.directions = ['z', 'q', 's', 'd']

    def maxcell_find(self):
        ''' Identifies the value of the maximum cell self.grid'''
        check = 0
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] > check:
                    check = self.grid[i][j]
        self.maxcell = check
        return self.maxcell

    def sup_2048(self):
        ''' Counts the amount of cells with value 
        greater than or equal to 2048'''
        count = 0
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] >= 2048:
                    count += 1
        self.goal = count
        return self.goal
    
    def newcell_start(self):
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
        self.grid[pos1][pos2] = new_cell
        return self.grid

    def newcell(self):
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
        ''' Display grid and score.

        see example:
                [0, 2, 2, 4]
                [0, 0, 4, 2]
                [4, 0, 2, 2]
                [8, 2, 4, 8]
                Your score is 32
        '''

        print(self.grid[0])
        print(self.grid[1])
        print(self.grid[2])
        print(self.grid[3])
        print(f'Your score is {self.score}')

    def possible_action(self):
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
        ''' Check every step if you lose to stop
        the game when there is no possible movement
        '''

        full_cell = 0
        for i in range(4):
            for j in range(4):
                if (self.grid[i][j] != 0):
                    full_cell += 1
        if (full_cell == 16 and not self.possible_action()):
            self.status = False
        return self.status

    def stack(self):
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
                if (self.grid[i][j] != 0):
                    new_grid[i][position] = self.grid[i][j]
                    position += 1
        self.grid = new_grid
        return self.grid

    def merge_left(self):
        ''' Merge grid to the left.

        see example:

            grid = [0, 2, 2, 0]  Become [0, 4, 0, 0]
                   [2, 4, 4, 2]         [2, 8, 0, 2]
                   [0, 2, 0, 4]         [0, 2, 0, 4]
                   [8, 8, 8, 8]         [16, 0, 16, 0]

        '''

        for i in range(4):
            for j in range(3):
                if(self.grid[i][j] == self.grid[i][j+1]):
                    self.grid[i][j] = self.grid[i][j] * 2
                    self.grid[i][j + 1] = 0
                    self.score += self.grid[i][j]
        return self.grid, self.score

    def transpose(self):
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
                new_grid[j][i] = self.grid[i][j]
        self.grid = new_grid
        return self.grid

    def inverse(self):
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
                new_grid[i][j] = self.grid[i][3-j]
        self.grid = new_grid
        return self.grid

    def left_movement(self):
        ''' Move grid to the left

        see example:

            grid = [2, 2, 0, 0]  Become [4, 0, 0, 0]
                   [0, 0, 2, 2]         [4, 0, 0, 0]
                   [0, 0, 0, 2]         [2, 0, 0, 0]
                   [4, 4, 0, 2]         [8, 2, 0, 0]
        '''

        self.stack()
        self.merge_left()
        self.stack()
        return self.grid, self.score

    def up_movement(self):
        ''' Move grid to the top

        see example:

            grid = [2, 2, 0, 0]  Become [2, 2, 2, 4]
                   [0, 0, 2, 2]         [4, 4, 0, 2]
                   [0, 0, 0, 2]         [0, 0, 0, 0]
                   [4, 4, 0, 2]         [0, 0, 0, 0]
        '''

        self.transpose()
        self.stack()
        self.merge_left()
        self.stack()
        self.transpose()
        return self.grid, self.score

    def down_movement(self):
        ''' Move grid to the botom

        see example:

            grid = [2, 2, 0, 0]  Become [0, 0, 0, 0]
                   [0, 0, 2, 2]         [0, 0, 0, 0]
                   [0, 0, 0, 2]         [2, 2, 0, 2]
                   [4, 4, 0, 2]         [4, 4, 2, 4]
        '''

        self.transpose()
        self.inverse()
        self.stack()
        self.merge_left()
        self.stack()
        self.inverse()
        self.transpose()
        return self.grid, self.score

    def right_movement(self):
        ''' Move grid to the right

        see example:

            grid = [2, 2, 0, 0]  Become [0, 0, 0, 4]
                   [0, 0, 2, 2]         [0, 0, 0, 4]
                   [0, 0, 0, 2]         [0, 0, 0, 2]
                   [4, 4, 0, 2]         [0, 0, 8, 2]
        '''

        self.inverse()
        self.left_movement()
        self.inverse()
        return self.grid, self.score

    def main(self):
        ''' Main game lauch this function to play
        The command are classical  zqsd (azerty keybord)
        Command : z => up
        Command : q => left
        Command : d => right
        Command : s => down
        to do an action you must select a direction and  press enter
        to quit write "quit" and press enter
        '''
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


    def demo(self):
        """ Demo of an AI game (displayed)

        """
        directions = ['z', 'q', 's', 'd']
        self.newcell_start()
        self.newcell()
        self.display()

        while(self.status):
            time.sleep(2)
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
            self.stop_game()
            if self.status and self.grid != grid_test:
                self.newcell()
            self.display()
            print(f'IA lost play {x} movement')
            if self.status is False:
                print(f'IA lost is score is {self.score}')
    
    
    
    def random_2048(self):
        """ AI game with random movements only.

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
        """ AI game with clockwise movement (starting movement
         is randomized)

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
            

# Lauch_game = Game()
# print('Command : z => up')
# print('Command : q => left')
# print('Command : d => right')
# print('Command : s => down')
# print('to do an action you must select a direction and  press enter')
# Lauch_game.main() # Lauch game


class Game_6561():
    """ This class represent gamegrid and function"""

    def __init__(self):
        """ Create new grid """
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.score = 0
        self.status = True

    def newcell_start(self):
        ''' Add new cell to the grid when grid is empty.
            Probability are 1/10 to be a 6
                            9/10 to be a 3

        see example:

            grid [0, 0, 0]  Become  [0, 0, 3]
                 [0, 0, 0]          [0, 0, 0]
                 [0, 0, 0]          [0, 0, 0]
                           
        '''

        new_cell = 3
        pos1 = random.randint(a=0, b=2)
        pos2 = random.randint(a=0, b=2)
        if random.uniform(a=0, b=1) > 0.90:
            new_cell = 6
        self.grid[pos1][pos2] = new_cell
        return self.grid

    def newcell(self):
        ''' Add new cell to the grid.
            Probability are  1/10 to be a 6
                             9/10 to be a 3

        see example:

            grid [0, 3, 3]  Become  [3, 3, 0]
                 [0, 0, 0]          [0, 0, 0]
                 [0, 0, 0]          [0, 6, 0]
                           
        '''

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
        ''' Display grid and score.

        see example:

                [0, 3, 0]
                [0, 0, 0]
                [0, 0, 3]
                
                Your score is 6
        '''

        print(self.grid[0])
        print(self.grid[1])
        print(self.grid[2])
        print(f'Your score is {self.score}')

    def possible_action(self):
        '''Checks if a movement is possible on the grid'''
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
        ''' Check every step if you lose to stop
        the game when there is no possible movement
        '''

        full_cell = 0
        for i in range(3):
            for j in range(3):
                if (self.grid[i][j] != 0):
                    full_cell += 1
        if (full_cell == 9 and not self.possible_action()):
            self.status = False
        return self.status

    def stack(self):
        ''' Stack the grid to the left.

        see example:

            grid [0, 3, 0]  Become  [3, 0, 0]
                 [0, 0, 0]          [0, 0, 0]
                 [9, 0, 0]          [9, 0, 0]
                        
        '''

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
        ''' Merge grid to the left.

        see example:

            grid = [0, 3, 3]  Become [0, 9, 0]
                   [9, 9, 0]         [27, 0, 0]
                   [0, 0, 3]         [0, 0, 3]
                        

        '''

        for i in range(3):
            for j in range(2):
                if(self.grid[i][j] == self.grid[i][j+1]):
                    self.grid[i][j] = self.grid[i][j] * 3
                    self.grid[i][j + 1] = 0
                    self.score += self.grid[i][j]
        return self.grid, self.score

    def transpose(self):
        ''' Transpose the grid, usefull to make movement.
        All movement are base on left merge, left stack

        see example:

            grid = [3, 3, 3]  Become [3, 0, 0]
                   [0, 3, 3]         [3, 3, 0]
                   [0, 0, 3]         [3, 3, 3]
                   
        '''

        new_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                new_grid[j][i] = self.grid[i][j]
        self.grid = new_grid
        return self.grid

    def inverse(self):
        ''' Inverse the grid, usefull to make movement.
        All movement are base on left merge, left stack

        see example:

            grid = [3, 3, 3]  Become [3, 3, 3]
                   [0, 3, 3]         [3, 3, 3]
                   [0, 0, 3]         [3, 3, 0]
                
        '''

        new_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                new_grid[i][j] = self.grid[i][2-j]
        self.grid = new_grid
        return self.grid

    def left_movement(self):
        ''' Move grid to the left

        see example:

            grid = [6, 0, 6]  Become [9, 0, 0]
                   [0, 0, 6]         [6, 0, 0]
                   [0, 0, 3]         [3, 0, 0]
        '''

        self.stack()
        self.merge_left()
        self.stack()
        return self.grid, self.score

    def up_movement(self):
        ''' Move grid to the top

        see example:

            grid = [3, 3, 0]  Become [3, 3, 3]
                   [0, 0, 3]         [9, 9, 0]
                   [0, 9, 0]         [0, 0, 0]
                            
        '''
        
        self.transpose()
        self.stack()
        self.merge_left()
        self.stack()
        self.transpose()
        return self.grid, self.score

    def down_movement(self):
        ''' Move grid to the botom

        see example:

            grid = [9, 9, 0]  Become [0, 0, 0]
                   [0, 0, 3]         [0, 0, 0]
                   [0, 0, 0]         [9, 9, 3]

        '''

        self.transpose()
        self.inverse()
        self.stack()
        self.merge_left()
        self.stack()
        self.inverse()
        self.transpose()
        return self.grid, self.score

    def right_movement(self):
        ''' Move grid to the right

        see example:

            grid = [3, 3, 0]  Become [0, 0, 9]
                   [0, 0, 3]         [0, 0, 3]
                   [9, 0, 3]         [0, 9, 3]
                   
        '''

        self.inverse()
        self.left_movement()
        self.inverse()
        return self.grid, self.score

    def main(self):
        ''' Main game lauch this function to play
        The command are classical  zqsd (azerty keybord)
        Command : z => up
        Command : q => left
        Command : d => right
        Command : s => down
        to do an action you must select a direction and  press enter
        to quit write "quit" and press enter
        '''
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


#AAA = Game_2048().clockwise_2048()
#AAA.random_2048()
#print(AAA.score)