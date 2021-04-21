import Game2048.Main as Main
import random
import time

# This script show battle of two IA playing strategies that you want
# We dont use class fonction because difficult to plot
# two game at the game time.
# This script isn't pep8 beacause of graphical display.


# empirical values
random_empirical_mean = 1095
clockwise_empirical_mean = 2310
opposite_empirical_mean = 88
adjacent_empirical_mean = 120


def launch_versus():
    """
    Create two grid
    """

    AI_one = Main.Game_2048()
    AI_two = Main.Game_2048()

    AI_one.newcell_start()
    AI_one.newcell()
    AI_two.newcell_start()
    AI_two.newcell()

    return AI_one, AI_two


def set_random_position():
    """
    Set random the opposite and adjacent strategies
    up/down or right/left and up/left or down/right
    """

    seed = random.random()
    if seed > 0.5:
        two_opposite = ['z', 's']
        two_adjacent = ['z', 'q']
    if seed <= 0.5:
        two_opposite = ['q', 'd']
        two_adjacent = ['s', 'd']

    return two_opposite, two_adjacent


def scoreboard(grid1, grid2, strategy1, strategy2):
    """
    Set scorebord att the end of the game
    """
    # Set graphical ---- to improve visibility
    print('--------------------------------------------------------------------------------------------------------------------')
    average1 = ''
    average2 = ''
    strategy_win = ''

    # Find the winner

    if grid1.score < grid2.score:
        strategy_win = strategy2
    else:
        strategy_win = strategy1
    if(grid1.score < grid2.score):
        print(f"AI_two win this game, {strategy2} strategy won this time,")
        print('')
    else:
        print(f"AI_one win this game, {strategy1} strategy won this time,")
        print('')

    # Display lucky score if the score is superior to the empirical mean
    # Calulated in orther script

    if grid1.score > random_empirical_mean and strategy1 == 'random':
        average1 = ", lucky score !"
    if grid2.score > random_empirical_mean and strategy2 == 'random':
        average2 = ", lucky score !"

    if grid1.score > clockwise_empirical_mean and strategy1 == 'clockwise':
        average1 = ", lucky score !"
    if grid2.score > clockwise_empirical_mean and strategy2 == 'clockwise':
        average2 = ", lucky score !"

    print(f"The final score for AI_one is {grid1.score}{average1}")
    print(f"The final score for AI_two is {grid2.score}{average2}")
    print('')

    if strategy_win == 'clockwise':
        print(f'The empirical mean with the {strategy_win} strategy is {clockwise_empirical_mean} and the empirical variance is ')
    if strategy_win == 'random':
        print(f'The empirical mean with the {strategy_win} strategy is {random_empirical_mean} and the empirical variance is ')

    if strategy_win == 'opposite':
        print(f'The empirical mean with the {strategy_win} strategy is {opposite_empirical_mean} and the empirical variance is ')

    if strategy_win == 'adjacent':
        print(f'The empirical mean with the {strategy_win} strategy is {adjacent_empirical_mean} and the empirical variance is ')
    print('--------------------------------------------------------------------------------------------------------------------')


def state_game2(grid1, grid2, x="", y="", strategy1="", strategy2=""):
    """
    Display the grid's state,
    status of game, play made, score and strategy playing.
    """
    print("--------------------------------------------------------------------")
    print(f'AI_one play: {x}                          AI_two play: {y}')
    print("\n")
    print(f"{grid1.grid[0]}                            {grid2.grid[0]}")
    print(f"{grid1.grid[1]}                            {grid2.grid[1]}")
    print(f"{grid1.grid[2]}                            {grid2.grid[2]}")
    print(f"{grid1.grid[3]}                            {grid2.grid[3]}")
    print(f"AI_one score is {grid1.score}                      AI_two score is {grid2.score}")
    print(f"AI_one play {strategy1} strategy            AI_two play {strategy2} strategy")

    return('------------')


def Versus(strategy1='random', strategy2='random', skip=False, speed=0.5):
    """
    You can chose among 4 strategies and compare the point.

    :param strategy1: First strategy, default = 'random'
    :type strategy1: str
    :param strategy2: Second strategy, default = 'random'
    :type strategy2: str
    :param Skip: Skip the display, only show the result, default = 'False'
    :type Skip: boolean
    :param speed: Display speed, default = '0.5'
    :type speed: float

    - Random : IA playing random movement
    - Clockwise : IA playing clockwise movement
    - Adjacent : IA playing only two adjacent movement
    - Opposite : IA playing only two opposite movement


    """
    # Set random position to adjacent and opposite strategies
    two_opposite, two_adjacent = set_random_position()
    AI_one, AI_two = launch_versus()

    if skip is False:
        state_game2(AI_one, AI_two)

    x = random.choice(AI_one.directions)
    y = random.choice(AI_two.directions)

    # Counter use to check if game bug or to do some statistical results
    block_game1 = 0
    block_game2 = 0
    nb_movement = 0
    movement_play1 = 0
    movement_play2 = 0

    while(AI_one.status or AI_two.status):

        # Check for two IA the moove to make
        # in function of which strategies there are
        # playing.
        # We can improve the code here...
        if strategy1 == 'random':
            x = random.choice(AI_one.directions)
        if strategy2 == 'random':
            y = random.choice(AI_two.directions)

        if strategy1 == 'clockwise':
            x = AI_one.directions[AI_one.directions.index(x) - 1]
        if strategy2 == 'clockwise':
            y = AI_two.directions[AI_two.directions.index(y) - 1]

        if strategy1 == 'opposite':
            x = two_opposite[movement_play1]
            movement_play1 = (movement_play1 + 1) % 2

        if strategy2 == 'opposite':
            y = two_opposite[movement_play2]
            movement_play2 = (movement_play2 + 1) % 2

        if strategy1 == 'adjacent':
            x = two_adjacent[movement_play1]
            movement_play1 = (movement_play1 + 1) % 2

        if strategy2 == 'adjacent':
            y = two_adjacent[movement_play2]
            movement_play2 = (movement_play2 + 1) % 2

        # Check if grid changed

        grid_test1 = AI_one.grid
        grid_test2 = AI_two.grid

        if (x.upper() == 'D'):
            AI_one.right_movement()
        if (x.upper() == 'Z'):
            AI_one.up_movement()
        if (x.upper() == 'S'):
            AI_one.down_movement()
        if (x.upper() == 'Q'):
            AI_one.left_movement()
        if (y.upper() == 'D'):
            AI_two.right_movement()
        if (y.upper() == 'Z'):
            AI_two.up_movement()
        if (y.upper() == 'S'):
            AI_two.down_movement()
        if (y.upper() == 'Q'):
            AI_two.left_movement()
        
        AI_one.stop_game()
        AI_two.stop_game()

        if AI_one.status and AI_one.grid != grid_test1:
            AI_one.newcell()
        if AI_two.status and AI_two.grid != grid_test2:
            AI_two.newcell()

        # Check if the game is block, with this two strategies
        # game bug many time because of the weekness of moovement 
        # it can block and do the same movement in boucle so we stop
        # the game when it repeat the same movement three time
        # ie it can't make other moove or improve is score

        if strategy1 == 'opposite' or strategy1 == 'adjacent':
            if AI_one.grid == grid_test1:
                block_game1 += 1
            if block_game1 > 3:
                AI_one.status = False

        if strategy2 == 'opposite' or strategy2 == 'adjacent':
            if AI_two.grid == grid_test2:
                block_game2 += 1
            if block_game2 > 3:
                AI_two.status = False

        # skip display or not

        if skip is False:
            state_game2(AI_one, AI_two, x, y, strategy1, strategy2)
            time.sleep(speed)
        nb_movement += 1

        # Stop the game if number of movement are to high
        # If 4000 movement happend with IA playing is necessarily
        # a bug mean number of movement play are near 300 movement.

        if nb_movement > 4000:
            AI_one.status = False
            AI_two.status = False

    scoreboard(AI_one, AI_two, strategy1, strategy2)

