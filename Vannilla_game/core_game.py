# Core game
import Fonction_2048 as fonc 

grid = fonc.new_game()
game_over = True
fonc.state_game(grid) 
score = 0


# Display command
print('Command : z => up')
print('Command : q => left')
print('Command : d => right')
print('Command : s => down')
print('to do an action you must select a direction and  pres enter')


# Core game
while(game_over):
    x = input('press command')

    if (x == 'd' or x == 'D') :
        grid = fonc.right_movement(grid)
    if (x == 'z' or x == 'Z'):
        grid = fonc.up_movement(grid)
    if (x == 's' or x == 'S'):
        grid = fonc.down_movement(grid)
    if (x == 'q' or x == 'q'):
        grid = fonc.left_movement(grid)
    final = fonc.stop_game(grid)
    if final == False:
        game_over = False
    if final == True:
        grid = fonc.newcell(grid)
    fonc.state_game(grid)

if game_over == False:
    print(f'your loose your score is {score}')   
