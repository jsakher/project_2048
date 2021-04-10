import random
import numpy as np
import matplotlib.pyplot as plt


just_calcul = True

class Game():
    """ This class represent gamegrid and function"""

    def __init__(self):
        """ Create new grid """
        self.grid = [[0, 0, 0, 0], [0, 0, 0, 0],
                     [0, 0, 0, 0], [0, 0, 0, 0]]
        self.score = 0
        self.status = True

    
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

    
    def stop_game(self):
        ''' Check every step if you lose to stop
        the game when there is no possible movement
        '''

        full_cell = 0
        for i in range(4):
            for j in range(4):
                if (self.grid[i][j] != 0):
                    full_cell += 1
        if full_cell == 16:
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
        count = 0
        

        while(self.status):
            
            x = "q"
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
            if self.status:
                self.newcell()
        count = (count + 1) % 2
        

count = 0
if just_calcul is False:
    Lauch_game = Game()
    Lauch_game.main() # Lauch game

    print(Lauch_game.score)

    stockage_score = []
    for i in range(1500):
        AI_play = Game()
        AI_play.main()
        stockage_score.append(AI_play.score)
        count = (count + 1) % 2
        print(i)


    Data_raw = np.array(stockage_score)
    np.savetxt('./Data_storage/Storage_AI_score_left.txt', Data_raw)

else:

    Data_score_up = np.loadtxt('./Data_storage/Storage_AI_score_up.txt')
    Data_score_down = np.loadtxt('./Data_storage/Storage_AI_score_down.txt')
    Data_score_left = np.loadtxt('./Data_storage/Storage_AI_score_left.txt')
    Data_score_right = np.loadtxt('./Data_storage/Storage_AI_score_right.txt')


    Mean_storage_up = (1/np.arange(1, len(Data_score_up)+1)) * np.cumsum(Data_score_up)
    Mean_storage_down = (1/np.arange(1, len(Data_score_down)+1)) * np.cumsum(Data_score_down)
    Mean_storage_left = (1/np.arange(1, len(Data_score_left)+1)) * np.cumsum(Data_score_left)
    Mean_storage_right = (1/np.arange(1, len(Data_score_right)+1)) * np.cumsum(Data_score_right)





    plt.figure()
    plt.plot(Mean_storage_up, color='#FF8C00', label='up movement')
    plt.plot(Mean_storage_left, color='#DC143C', label='left movement')
    plt.plot(Mean_storage_right, color='#6495ED', label='right movement')
    plt.plot(Mean_storage_down, color='#da70d6', label='down movement')
    plt.legend()
    plt.xlim(0, 1500)
    plt.ylim(100,300)
    # plt.plot(Mean_storage, color='#FF8C00')
    # plt.label('Random movement')
    plt.savefig('./Data_storage/AI_score_onemovement.pdf')
    plt.show()

