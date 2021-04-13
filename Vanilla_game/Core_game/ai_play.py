import Fonction_2048 as fonc 
import random

def ai_right():
    global game_over, score

    print('Initial grid:')
    grid = fonc.new_game()
    game_over = True
    score = 0
    fonc.state_game(grid, score) 
    
    print('Strategies:')
    print(' - right movement')
    print(' - random movement')
    print(' - left movement')
    print(' - clockwise movement')

    strategy = input('Choose a strategy :')

    if strategy == 'right movement':
        while(game_over):

            x = 'd'
            
            if (x == 'd' or x == 'D') :
                grid, score = fonc.right_movement(grid, score)
            if (x == 'z' or x == 'Z'):
                grid, score = fonc.up_movement(grid, score)
            if (x == 's' or x == 'S'):
                grid, score = fonc.down_movement(grid, score)
            if (x == 'q' or x == 'q'):
                grid, score = fonc.left_movement(grid, score)
            final = fonc.stop_game(grid)
            if final == False:
                game_over = False
            if final == True:
                grid = fonc.newcell(grid)
            fonc.state_game(grid, score)
            print('--------------')

    if strategy == 'random movement':
        while(game_over):

            directions = ['z', 'q', 's', 'd']
            x = random.choice(directions)
            if x == 'z':
                print('up')
            elif x == 'd':
                print('right')
            elif x == 's':
                print('down')
            else:
                print('left')

            print('--------------')

            if (x == 'd' or x == 'D') :
                grid, score = fonc.right_movement(grid, score)
            if (x == 'z' or x == 'Z'):
                grid, score = fonc.up_movement(grid, score)
            if (x == 's' or x == 'S'):
                grid, score = fonc.down_movement(grid, score)
            if (x == 'q' or x == 'q'):
                grid, score = fonc.left_movement(grid, score)
            final = fonc.stop_game(grid)
            if final == False:
                game_over = False
            if final == True:
                grid = fonc.newcell(grid)
            fonc.state_game(grid, score)
            print('--------------')

    if strategy == 'left movement':
        while(game_over):

            x = 'q'
            
            if (x == 'd' or x == 'D') :
                grid, score = fonc.right_movement(grid, score)
            if (x == 'z' or x == 'Z'):
                grid, score = fonc.up_movement(grid, score)
            if (x == 's' or x == 'S'):
                grid, score = fonc.down_movement(grid, score)
            if (x == 'q' or x == 'q'):
                grid, score = fonc.left_movement(grid, score)
            final = fonc.stop_game(grid)
            if final == False:
                game_over = False
            if final == True:
                grid = fonc.newcell(grid)
            fonc.state_game(grid, score)

    if strategy == 'clockwise movement':

        directions = ['z', 'q', 's', 'd']
        x = random.choice(directions) 

        while(game_over):

            if x == 'z':
                x = 'd'
                print('right')
            elif x == 'd':
                x = 's'
                print('down')
            elif x == 's':
                x = 'q'
                print('left')
            else:
                x = 'z'
                print('up')
            
            print('--------------')

            if (x == 'd' or x == 'D') :
                grid, score = fonc.right_movement(grid, score)
            if (x == 'z' or x == 'Z'):
                grid, score = fonc.up_movement(grid, score)
            if (x == 's' or x == 'S'):
                grid, score = fonc.down_movement(grid, score)
            if (x == 'q' or x == 'q'):
                grid, score = fonc.left_movement(grid, score)
            final = fonc.stop_game(grid)
            if final == False:
                game_over = False
            if final == True:
                grid = fonc.newcell(grid)
            fonc.state_game(grid, score)
            print('--------------')

    if game_over == False:
        print(f'you loose your score is {score}')

def main():
    while (True):
        ai_right()
        break
if __name__ == '__main__':
    main()