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
print('to do an action you must select a direction and  press enter')


# Core game
while(game_over):
    x = input('press command')
    #x.upper() #transforming the string command to uppercase to easily check the following conditions.

    if (x.upper() == 'D') :
        grid = fonc.right_movement(grid)
    if (x.upper() == 'Z'):
        grid = fonc.up_movement(grid)
    if (x.upper() == 'S'):
        grid = fonc.down_movement(grid)
    if (x.upper() == 'Q'):
        grid = fonc.left_movement(grid)
    final = fonc.stop_game(grid)
    if (x.upper() == 'QUIT'): #Allows the player to quit the game, and print the score.
        game_over = False
    if final == False:
        game_over = False
    if final == True:
        grid = fonc.newcell(grid)
    fonc.state_game(grid)

if game_over == False:
    print(f'you loose your score is {score}')   
