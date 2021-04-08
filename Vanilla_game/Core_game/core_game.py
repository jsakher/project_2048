# Core game
import Fonction_2048 as fonc 

grid = fonc.new_game()
game_over = True
score = 0
fonc.state_game(grid, score) 



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

    ## Movements-wise : No movement should be allowed if there's is not existing cell to move; an error needs to be raised in such case.
    if (x.upper() == 'D') : 
        grid, score = fonc.right_movement(grid, score)
    if (x.upper() == 'Z'):
        grid, score = fonc.up_movement(grid, score)
    if (x.upper() == 'S'):
        grid, score = fonc.down_movement(grid, score)
    if (x.upper() == 'Q'):
        grid, score = fonc.left_movement(grid, score)
    if (x.upper() == 'QUIT'): #Allows the player to quit the game, and print the score.
        game_over = False
    final = fonc.stop_game(grid)
    if final == False:
        game_over = False
    if final == True:
        grid = fonc.newcell(grid)
    fonc.state_game(grid, score)

if game_over == False:
    print(f'you lose your score is {score}')   
