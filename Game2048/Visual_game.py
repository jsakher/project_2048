from tkinter import Tk, Canvas, Label, Button, LEFT
import Fonction_2048 as fonc
import Main


def Visual_game(colorblind=False):

    """
    Creates a visualization of  the 2048 game, it uses tkinter package
    that enchance game. This version use Fonction_2048 script which functions
    are set without class type (because incompatible with tkinter framework)

    Colorblind color game: all cell have blue or yellow color (no green/red)
    """

    # Create a list with color usefull for the grid

    colorlist = []
    for i in range(2049):
        colorlist.append('#000000')

    if colorblind is False:
        colorlist[0] = '#FCF3CF'
        colorlist[2] = '#5DADE2'
        colorlist[4] = '#2874A6'
        colorlist[8] = '#EB984E'
        colorlist[16] = '#D35400'
        colorlist[32] = '#E74C3C'
        colorlist[64] = '#58D68D'
        colorlist[128] = '#16A085'
        colorlist[256] = '#A569BD'
        colorlist[512] = '#633974'
        colorlist[1024] = '#edc53f'
        colorlist[2048] = '#edc22d'
    else:
        colorlist[0] = '#FFFFFF'
        colorlist[2] = '#ADD8E6'
        colorlist[4] = '#BDB76B'
        colorlist[8] = '#1E90FF'
        colorlist[16] = '#FFD700'
        colorlist[32] = '#a3a2db'
        colorlist[64] = '#d473d4'
        colorlist[128] = '#FFFF00'
        colorlist[256] = '#4682B4'
        colorlist[512] = '#FFD700'
        colorlist[1024] = '#FFFACD'
        colorlist[2048] = '#0000FF'

    color_cell1 = colorlist

    # Run algorithm and get score to challenge the player and
    # display algorithm's score in game window.

    AI_random = Main.Game_2048()
    AI_random.random_2048()
    AI_clockwise = Main.Game_2048()
    AI_clockwise.clockwise_2048()

    # Creation of tkinter window set size and icon
    window = Tk()
    window.title("2048")
    window.geometry("720x480")
    window.minsize(720, 480)
    window.iconbitmap("./Game2048/ico2048.ico")
    window.config(background='#B0C4DE')
    width = 400
    height = 400
    Canevas = Canvas(window, width=width, height=height, bg='black')
    Canevas.pack(padx=5, pady=5)

    # Set the grid
    grid = fonc.new_game()
    game_over = True
    final_score = 0
    # Display command to the player
    print('Command : z => up')
    print('Command : q => left')
    print('Command : s => down')
    print('Command : d => right')
    print('')
    print('to do an action you must select a direction and  press enter')
    print('play in terminal and see grid in the popup window')

    # Graphics settings, add labbel to tkinter window
    """
    This part sets axes to construct the grid and scoreboard display.
    """
    # Set scoreboard

    score_display = Label(window, bd=14, bg='#B0C4DE',
                          text='Your score is : ',
                          font=('Helvetica', 13, 'bold'))
    score_display.place(x=10, y=20)
    score_display = Label(window, bd=15, bg='#B0C4DE',
                          text=final_score,
                          font=('Helvetica', 15, 'bold'))
    score_display.place(x=50, y=60)

    # Set axes
    # --------------------------------------------------------

    Lab_0_0 = Label(window, bd=30, bg=color_cell1[grid[0][0]],
                    text=(grid[0][0]),
                    font=100)
    Lab_0_0.place(x=190, y=20)

    Lab_0_1 = Label(window, bd=30, bg=color_cell1[grid[0][1]],
                    text=(grid[0][1]),
                    font=400)
    Lab_0_1.place(x=275, y=20)

    Lab_0_2 = Label(window, bd=30, bg=color_cell1[grid[0][2]],
                    text=(grid[0][2]),
                    font=200)
    Lab_0_2.place(x=365, y=20)

    Lab_0_3 = Label(window, bd=30, bg=color_cell1[grid[0][3]],
                    text=(grid[0][3]),
                    font=300)
    Lab_0_3.place(x=450, y=20)
    # ----------------------------------------------------------
    Lab_1_0 = Label(window, bd=30, bg=color_cell1[grid[1][0]],
                    text=(grid[1][0]),
                    font=25)
    Lab_1_0.place(x=190, y=120)

    Lab_1_1 = Label(window, bd=30, bg=color_cell1[grid[1][1]],
                    text=(grid[1][1]),
                    font=25)
    Lab_1_1.place(x=275, y=120)

    Lab_1_2 = Label(window, bd=30, bg=color_cell1[grid[1][2]],
                    text=(grid[1][2]),
                    font=25)
    Lab_1_2.place(x=365, y=120)

    Lab_1_3 = Label(window, bd=30, bg=color_cell1[grid[1][3]],
                    text=(grid[1][3]),
                    font=25)
    Lab_1_3.place(x=450, y=120)

    # ----------------------------------------------------------

    Lab_2_0 = Label(window, bd=30, bg=color_cell1[grid[2][0]],
                    text=(grid[2][0]),
                    font=25)
    Lab_2_0.place(x=190, y=220)

    Lab_2_1 = Label(window, bd=30, bg=color_cell1[grid[2][1]],
                    text=(grid[2][1]),
                    font=25)
    Lab_2_1.place(x=275, y=220)

    Lab_2_2 = Label(window, bd=30, bg=color_cell1[grid[2][2]],
                    text=(grid[2][2]),
                    font=25)
    Lab_2_2.place(x=365, y=220)

    Lab_2_3 = Label(window, bd=30, bg=color_cell1[grid[2][3]],
                    text=(grid[2][3]),
                    font=25)
    Lab_2_3.place(x=450, y=220)

    # ----------------------------------------------------------

    Lab_3_0 = Label(window, bd=30, bg=color_cell1[grid[3][0]],
                    text=(grid[3][0]),
                    font=25)
    Lab_3_0.place(x=190, y=310)

    Lab_3_1 = Label(window, bd=30, bg=color_cell1[grid[3][1]],
                    text=(grid[3][1]),
                    font=25)
    Lab_3_1.place(x=275, y=310)

    Lab_3_2 = Label(window, bd=30, bg=color_cell1[grid[3][2]],
                    text=(grid[3][2]),
                    font=25)
    Lab_3_2.place(x=365, y=310)

    Lab_3_3 = Label(window, bd=30, bg=color_cell1[grid[3][3]],
                    text=(grid[3][3]),
                    font=25)
    Lab_3_3.place(x=450, y=310)

    # ----------------------------------------------------------

    # IA score Display on the scoreboard
    clockwise_score_IA1 = Label(window, bd=5, bg='#B0C4DE',
                                text='Clockwise IA score:',
                                font=('Helvetica', 12, 'bold'))
    clockwise_score_IA1.place(x=560, y=210)
    clockwise_score_IA2 = Label(window, bd=2, bg='#B0C4DE',
                                text=AI_clockwise.score,
                                font=('Helvetica', 13, 'bold'))
    clockwise_score_IA2.place(x=620, y=250)

    Random_score_IA1 = Label(window, bd=15, bg='#B0C4DE',
                             text='Random IA score:',
                             font=('Helvetica', 13, 'bold'))
    Random_score_IA1.place(x=560, y=310)
    Random_score_IA2 = Label(window, bd=2, bg='#B0C4DE',
                             text=AI_random.score,
                             font=('Helvetica', 13, 'bold'))
    Random_score_IA2.place(x=620, y=350)

    # Quit button

    Button(window, text="Quit", bg='#FFFFFF',
           command=window.destroy).pack(side=LEFT, padx=5, pady=5)

    # Main loop

    while(game_over):

        x = input('press command ')
        grid_changed = grid  # Grid that allow to check if grid change

        if (x == 'd' or x == 'D'):
            grid, final_score = fonc.right_movement(grid, final_score)
        if (x == 'z' or x == 'Z'):
            grid, final_score = fonc.up_movement(grid, final_score)
        if (x == 's' or x == 'S'):
            grid, final_score = fonc.down_movement(grid, final_score)
        if (x == 'q' or x == 'q'):
            grid, final_score = fonc.left_movement(grid, final_score)
        final = fonc.stop_game(grid)
        if final is False:
            game_over = False
        if final is True and grid != grid_changed:
            grid = fonc.newcell(grid)

    # Grid and score actualization
    # ----------------------------------------------------------
        score_display.config(text=final_score)

        Lab_0_0.config(bg=color_cell1[grid[0][0]], text=(grid[0][0]))
        Lab_0_1.config(bg=color_cell1[grid[0][1]], text=(grid[0][1]))
        Lab_0_2.config(bg=color_cell1[grid[0][2]], text=(grid[0][2]))
        Lab_0_3.config(bg=color_cell1[grid[0][3]], text=(grid[0][3]))

    # ----------------------------------------------------------

        Lab_1_0.config(bg=color_cell1[grid[1][0]], text=(grid[1][0]))
        Lab_1_1.config(bg=color_cell1[grid[1][1]], text=(grid[1][1]))
        Lab_1_2.config(bg=color_cell1[grid[1][2]], text=(grid[1][2]))
        Lab_1_3.config(bg=color_cell1[grid[1][3]], text=(grid[1][3]))

    # ----------------------------------------------------------

        Lab_2_0.config(bg=color_cell1[grid[2][0]], text=(grid[2][0]))
        Lab_2_1.config(bg=color_cell1[grid[2][1]], text=(grid[2][1]))
        Lab_2_2.config(bg=color_cell1[grid[2][2]], text=(grid[2][2]))
        Lab_2_3.config(bg=color_cell1[grid[2][3]], text=(grid[2][3]))

    # ----------------------------------------------------------

        Lab_3_0.config(bg=color_cell1[grid[3][0]], text=grid[3][0])
        Lab_3_1.config(bg=color_cell1[grid[3][1]], text=grid[3][1])
        Lab_3_2.config(bg=color_cell1[grid[3][2]], text=grid[3][2])
        Lab_3_3.config(bg=color_cell1[grid[3][3]], text=grid[3][3])
    # ----------------------------------------------------------

        # Make png to make gif with edit_gif
        # script github:
        # Nathanesteve/Challenge_prediction/blob/main/Code_visualisation_Montpellier_cycliste/Edit_gif.py
        # im = pyscreenshot.grab(bbox=(5, 5, 720, 510))  # X1,Y1,X2,Y2
        # im.save("viusal_2048_{:03}.png".format(i))
        # i += 1

    if game_over is False:
        print(f'you lose your score is {final_score}')
        End = Label(window, bd=15, bg='#B0C4DE',
                    text='You lose. Your score is : ',
                    font=('Helvetica', 13, 'bold'))
        End.place(x=180, y=432)
        End_score = Label(window, bd=15, bg='#B0C4DE',
                          text=final_score,
                          font=('Helvetica', 13, 'bold'))
        End_score.place(x=390, y=432)
    window.mainloop()
