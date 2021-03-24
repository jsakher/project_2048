from tkinter import *
import tkinter
import Fonction_2048 as fonc

test_color = []
for i in range(2049):
    test_color.append('#000000')
test_color[0] = '#FCF3CF'
test_color[2] = '#5DADE2' #'#eee4da'
test_color[4] =  '#2874A6'           #'#ede0c8'
test_color[8] =  '#EB984E'      #'#f2b179'
test_color[16] =  '#D35400'     #'#f59563'
test_color[32] =  '#E74C3C '          #'#f67c60'
test_color[64] =   '#58D68D'           #'#f65e3b'
test_color[128] =  '#16A085'                #'#edcf73'
test_color[256] = '#A569BD'    #'#edcc62'
test_color[512] = '#633974 '  #'#edc850'
test_color[1024] = '#edc53f'
test_color[2048] = '#edc22d'
color_cell1 = test_color


window = Tk()
window.title("2048")
window.geometry("720x480")
window.minsize(720,480)
window.config(background='#FFFFFF')
position_grid = [(50,50), (150,50), (250,50), (350,50), (50,150),  (150,150), (250,150), (350,150), (50,250), (150,250), (250,250), (350,250), (50,350), (150,350), (250,350), (350,350)]
grid = fonc.new_game()
game_over = True
fonc.state_game(grid) 
score_final = 0
frame = Frame(window,background='#fef198')
gridc = "black"
game_over = True


# button1=tkinter.Button(window, text="left", command=fonc.left_movement(grid))
# button1.place(x=20, y=250)
# button1.configure(height = 2, width = 4)

# button2=tkinter.Button(window, text="right",command=fonc.right_movement(grid))
# button2.place(x=100, y=250)
# button2.configure(height = 2, width = 4)

# button3=tkinter.Button(window, text="up",command=fonc.up_movement(grid))
# button3.place(x=60, y=210)
# button3.configure(height = 2, width = 4)

# button3=tkinter.Button(window, text="down", command=fonc.down_movement(grid))
# button3.place(x=60, y=285)
# button3.configure(height = 2, width = 4)
Largeur = 400 
Hauteur = 400
Canevas = Canvas(window, width = Largeur, height =Hauteur, bg = 'black')
Canevas.pack(padx =5, pady =5)


Lab_0_0 = Label(window,bd = 30, bg=color_cell1[grid[0][0]],text=(grid[0][0]), font=100)
Lab_0_0.place(x=190,y=20)

Lab_0_1 = Label(window,bd = 30,bg=color_cell1[grid[0][1]], text=(grid[0][1]), font=400)
Lab_0_1.place(x=275,y=20)

Lab_0_2 = Label(window,bd = 30,bg=color_cell1[grid[0][2]], text=(grid[0][2]), font=200)
Lab_0_2.place(x=365,y=20)

Lab_0_3 = Label(window,bd = 30,bg=color_cell1[grid[0][3]], text=(grid[0][3]), font=300)
Lab_0_3.place(x=450,y=20)
# -------------------------------------------------
Lab_1_0 = Label(window,bd = 30,bg=color_cell1[grid[1][0]], text=(grid[1][0]), font=25)
Lab_1_0.place(x=190,y=120)

Lab_1_1 = Label(window,bd = 30,bg=color_cell1[grid[1][1]], text=(grid[1][1]), font=25)
Lab_1_1.place(x=275,y=120)

Lab_1_2 = Label(window,bd = 30,bg=color_cell1[grid[1][2]], text=(grid[1][2]), font=25)
Lab_1_2.place(x=365,y=120)

Lab_1_3 = Label(window,bd = 30, bg=color_cell1[grid[1][3]], text=(grid[1][3]), font=25)
Lab_1_3.place(x=450,y=120)

# -------------------------------------------------

Lab_2_0 = Label(window,bd = 30,bg=color_cell1[grid[2][0]], text=(grid[2][0]), font=25)
Lab_2_0.place(x=190,y=220)

Lab_2_1 = Label(window,bd = 30,bg=color_cell1[grid[2][1]], text=(grid[2][1]), font=25)
Lab_2_1.place(x=275,y=220)

Lab_2_2 = Label(window,bd = 30,bg=color_cell1[grid[2][2]], text=(grid[2][2]), font=25)
Lab_2_2.place(x=365,y=220)

Lab_2_3 = Label(window,bd = 30,bg=color_cell1[grid[2][3]], text=(grid[2][3]), font=25)
Lab_2_3.place(x=450,y=220)

# -------------------------------------------------

Lab_3_0 = Label(window,bd = 30,bg=color_cell1[grid[3][0]], text=(grid[3][0]), font=25)
Lab_3_0.place(x=190,y=310)

Lab_3_1 = Label(window,bd = 30,bg=color_cell1[grid[3][1]], text=(grid[3][1]), font=25)
Lab_3_1.place(x=275,y=310)

Lab_3_2 = Label(window,bd = 30,bg=color_cell1[grid[3][2]], text=(grid[3][2]), font=25)
Lab_3_2.place(x=365,y=310)

Lab_3_3 = Label(window,bd = 30,bg=color_cell1[grid[3][3]], text=(grid[3][3]), font=25)
Lab_3_3.place(x=450,y=310)

    
Button(window, text ="Quitter", command = window.destroy).pack(side=LEFT,padx=5,pady=5)
#window.mainloop()
#Mafenetre.destroy


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

    Lab_0_0.config(bg=color_cell1[grid[0][0]], text=(grid[0][0]))
    Lab_0_1.config(bg=color_cell1[grid[0][1]],text=(grid[0][1]))
    Lab_0_2.config(bg=color_cell1[grid[0][2]],text=(grid[0][2]))
    Lab_0_3.config(bg=color_cell1[grid[0][3]],text=(grid[0][3]))
 
# -------------------------------------------------

    Lab_1_0.config(bg=color_cell1[grid[1][0]],text=(grid[1][0]))
    Lab_1_1.config(bg=color_cell1[grid[1][1]],text=(grid[1][1]))
    Lab_1_2.config(bg=color_cell1[grid[1][2]],text=(grid[1][2]))
    Lab_1_3.config(bg=color_cell1[grid[1][3]],text=(grid[1][3]))

# -------------------------------------------------

    Lab_2_0.config(bg=color_cell1[grid[2][0]],text=(grid[2][0]))
    Lab_2_1.config(bg=color_cell1[grid[2][1]],text=(grid[2][1]))
    Lab_2_2.config(bg=color_cell1[grid[2][2]],text=(grid[2][2]))
    Lab_2_3.config(bg=color_cell1[grid[2][3]],text=(grid[2][3]))

# -------------------------------------------------

    Lab_3_0.config(bg=color_cell1[grid[3][0]],text=grid[3][0])
    Lab_3_1.config(bg=color_cell1[grid[3][1]],text=grid[3][1])
    Lab_3_2.config(bg=color_cell1[grid[3][2]],text=grid[3][2])
    Lab_3_3.config(bg=color_cell1[grid[3][3]],text=grid[3][3])

    
    
if game_over == False:
    print(f'you loose your score is {score_final}')   



#frame.pack(expand=YES)
window.mainloop()

