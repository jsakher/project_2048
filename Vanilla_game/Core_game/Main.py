import random

class Game():
    """ This class represent gamegrid """

    def __init__(self):
        """ Create new grid """
        self.grid = [[0, 0, 0, 0], [0, 0, 0, 0],
                     [0, 0, 0, 0], [0, 0, 0, 0]]
        self.score = 0
        self.status = True

    def merge(self, score):

        for i in range(4):
            for j in range(3):
                if(self.grid[i][j] == self.grid[i][j+1]):
                    self.grid[i][j] = self.grid[i][j] * 2
                    self.grid[i][j + 1] = 0
                self.score += self.grid[i][j]
        return self.grid, self.score

    def newcell_start(self):
        new_cell = 2
        pos1 = random.randint(a=0, b=3)
        pos2 = random.randint(a=0, b=3)
        if random.uniform(a=0, b=1) > 0.90:
            new_cell = 4
        self.grid[pos1][pos2] = new_cell
        return self.grid

    def newcell(self):

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
            todo +=1
        pos = random.randint(a=0, b=todo-1) 
        if len(empty_cell) == 0:
            pos = [0, 0]
        else :
            pos = empty_cell[pos]
        a, b = pos[0], pos[1]
        self.grid[a][b] = new_cell

        return self.grid
    
    def display(self):
        print(self.grid[0])
        print(self.grid[1])
        print(self.grid[2])
        print(self.grid[3])
        print(f'Your score is {self.score}')

    def stop_game(self): #Game stops when there is no possible movement to make (i.e. cannot merge any cells), not when the grid is full !
        ''' Check every step if you lose '''

        full_cell = 0
        for i in range(4):
            for j in range(4):
                if (self.grid[i][j] != 0):
                    full_cell += 1
        if full_cell == 16:
            self.status = False
        return self.status

    def stack(self):
        new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(4):
            position = 0
            for j in range(4):
                if (self.grid[i][j] != 0):
                    new_grid[i][position] = self.grid[i][j]
                    position += 1
        self.grid = new_grid
        return self.grid

    def  merge_left(self):
        ''' Merge the grid on the left  '''
        #reward = 0
        for i in range(4): 
            for j in range(3):
                if(self.grid[i][j] == self.grid[i][j+1]): # revoir ; A:"range(n) renvoie les n premiers integers en partant de 0 => range(3) contient les 3 premiers chiffres en partant de 0 " 
                    self.grid[i][j] = self.grid[i][j] * 2 # Aucune modification à faire donc.
                    self.grid[i][j + 1] = 0
                    self.score += self.grid[i][j]
        return self.grid, self.score 



    def  rotation(self):
        ''' Rotate the grid, usefull to make movement'''

        new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        
        for i in range(4):
            for j in range(4):
                new_grid[i][j] = self.grid[i][3-j]
        self.grid = new_grid
        return self.grid


    def transpose(self):
        
        new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
        for i in range(4): 
            for j in range(4): 
                new_grid[j][i] = self.grid[i][j]
        self.grid = new_grid
        return self.grid

    def inverse(self):
        ''' inverse the grid, usefull to make movement ''' 
        new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
        for i in range(4): 
            for j in range(4): 
                new_grid[i][j] = self.grid[i][3-j]
        self.grid = new_grid
        return self.grid

# All movement are base on rotation and left_movement (On peut optimiser les algo)

    def  left_movement(self):
        ''' Move grid to the left '''

        self.stack()
        self.merge_left()
        self.stack()
        return self.grid, self.score


    def up_movement(self):
        ''' Move grid to the top '''
        self.transpose()
        self.stack()
        self.merge_left()
        self.stack()
        self.transpose()
        return self.grid, self.score
        



    def down_movement(self):
        ''' Move grid to the botom '''
        self.transpose()
        self.inverse()
        self.stack()
        self.merge_left()
        self.stack()
        self.inverse()
        self.transpose()
        return self.grid, self.score


    def  right_movement(self):
        self.rotation()
        self.left_movement()
        self.rotation()
        return self.grid, self.score
        
    def main(self):
        self.newcell_start()
        self.newcell()
        self.display()

        while(self.status):
            x = input('press command')
            #x.upper() #transforming the string command to uppercase to easily check the following conditions.

            ## Movements-wise : No movement should be allowed if there's is not existing cell to move; an error needs to be raised in such case.
            if (x.upper() == 'D') : 
                self.right_movement()
            if (x.upper() == 'Z'):
                self.up_movement()
            if (x.upper() == 'S'):
                self.down_movement()
            if (x.upper() == 'Q'):
                self.right_movement()
            if (x.upper() == 'QUIT'): #Allows the player to quit the game, and print the score.
                self.status = False
            self.stop_game()
            if self.status == False:
                self.status = False
            if self.status == True:
                self.newcell()
            self.display()  
           

            if self.status == False:
                print(f'you lose your score is {score}') 
        




AAA = Game()
AAA.main()


