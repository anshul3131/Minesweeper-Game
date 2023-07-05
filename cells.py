from tkinter import Button
from tkinter import Label
import random
import para
import ctypes
import sys
class Cell:
    all = []
    cell_cnt_label = None
    cell_left = para.CELLCNT
    def __init__(self,x,y,is_mine = False):
        self.is_mine = is_mine
        self.cell_btn = None
        self.x = x
        self.y = y
        self.is_opened = False
        self.is_mined = False
        Cell.all.append(self)
    def create_btn(self,location):
        btn = Button(
            location,
            width = 8,
            height = 2
        )
        btn.bind('<Button-1>',self.left_click_actions) #Allow Left Click
        btn.bind('<Button-3>',self.right_click_actions)#Allow Right Click
        self.cell_btn = btn
    def create_cell_cnt_label(location):
        lbl = Label(
            location,
            bg = 'black',
            fg = 'white',
            text = f"Cells Left : {para.CELLCNT}",
            width = 12,
            height = 4,
            font = ("",30)
        )
        Cell.cell_cnt_label = lbl
    def left_click_actions(self,event):#Event for Left Click
        if(self.is_mine):
            return self.show_mine()
        else:
            if(self.numOfmines()==0):
                for cell in self.surrounded_cells():
                    cell.show_cell()
            return self.show_cell()
    def show_mine(self):
        self.cell_btn.configure(bg = 'red')
        ctypes.windll.user32.MessageBoxW(0,'You clicked on a mine','Game Over',0)
        sys.exit()
    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if(cell.x==x and cell.y==y):
                return cell
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y -1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells
    def numOfmines(self):
        cnt = 0
        for cell in self.surrounded_cells():
            if(cell.is_mine):
                cnt+=1
        return cnt
    def show_cell(self):
        if(not self.is_opened):
            self.cell_btn.configure(bg = 'SystemButtonFace')
            Cell.cell_left-=1
            Cell.cell_cnt_label.configure(text = Cell.cell_left)
            self.cell_btn.configure(text = self.numOfmines())
        self.is_opened = True
        if(Cell.cell_left==para.MINECNT):
            ctypes.windll.user32.MessageBoxW(0,'Congratulation','You won the game',0)
        self.cell_btn.unbind('<Button-1>')
        self.cell_btn.unbind('<Button-3>')
    def right_click_actions(self,event):#Event for Right Click
        if(not self.is_mined):
            self.cell_btn.configure(bg = 'yellow')
            self.is_mined = True
        else:
            self.cell_btn.configure(bg = 'SystemButtonFace')
            self.is_mined = False
    def randomized_mines():
        picked_mines = random.sample(Cell.all,para.MINECNT)
        for mines in picked_mines:
            mines.is_mine = True
    def __repr__(self):
        return f"Cell({self.x},{self.y})"