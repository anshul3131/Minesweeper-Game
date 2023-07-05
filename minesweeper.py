from tkinter import *
import para
import calc
from cells import Cell
root = Tk()
root.configure(bg="black")
root.geometry(f'{para.WIDTH}x{para.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False,False)
Top_Frame = Frame(
    root,
    bg = 'black',
    width = 1440,
    height = calc.percHeight(25)

)
Top_Frame.place(x = calc.percWidth(25),y = 0)
game_title = Label(
    Top_Frame,
    bg = 'black',
    fg = 'white',
    width = calc.percWidth(100),
    height = calc.percHeight(25),
    text = f"MINESWEEPER GAME",
    font = ("",20)
)
game_title.place(x = 0,y = 0)
Left_Frame = Frame(
    root,
    bg = 'black',
    width = calc.percWidth(25),
    height = calc.percHeight(75)
)
Left_Frame.place(x=0,y = calc.percHeight(25))
Center_Frame = Frame(
    root,
    bg = 'black',
    width = calc.percWidth(75),
    height = calc.percHeight(75)
)
Center_Frame.place(x = calc.percWidth(25),y = calc.percHeight(25))
for i in range(para.GRIDSIZE):
    for j in range(para.GRIDSIZE):
        c  = Cell(i,j)
        c.create_btn(Center_Frame)
        c.cell_btn.grid(row = i,column = j)
Cell.randomized_mines()
Cell.create_cell_cnt_label(Left_Frame)
Cell.cell_cnt_label.place(x = 0,y = 0)
root.mainloop()