from tkinter import *
from tkinter import ttk
import pygame

class startScreen:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.configure = Button(self.frame, text = "⚙ Configure", command = self.openConfigure)
        self.configure.pack()
        self.title = Label(self.frame, text = "Welcome")
        self.title.pack()
        self.current_loc = Button(self.frame, text = "VARIABLE TEXT HERE **LOC**", command = self.openLocSelector)
        self.current_loc.pack()
        self.sort_dist = Button(self.frame, text = "Distance", command = self.openSortDist)
        self.sort_dist.pack()
        self.sort_food = Button(self.frame, text = "Food", command = self.openSortFood)
        self.sort_food.pack()
        self.sort_rank = Button(self.frame, text = "Rank", command = self.openSortRank)
        self.sort_rank.pack()
        self.sort_price = Button(self.frame, text = "Price", command = self.openSortPrice)
        self.sort_price.pack()
        
    def openConfigure(self):
        #open separate configuration window
        #use pyforms?
        pass
    
    def openLocSelector(self):
        #retrieve location from map and show current location
        pass
    
    def openSortDist(self):
        self.newWindow = Toplevel(self.master)
        self.app = sortedListViewer(self.newWindow)
        
    def openSortFood(self):
        pass
    
    def openSortRank(self):
        pass
        
    def openSortPrice(self):
        pass

class sortedListViewer:
    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(self.master) #padding
        self.frame.grid(column = 0, row = 0, sticky = (N,W,E,S))
        self.master.grid_columnconfigure(0, weight = 1)
        self.master.grid_rowconfigure(0, weight = 1)
        
        #variables
        self.namelist = ('Canteen 1', 'Canteen 2', 'Canteen 4', 'Canteen 9')
        self.lnames = StringVar(value=self.namelist)
        self.nameof = StringVar(value = "Name of Canteen: ")
        
        #widgets
        self.lbox = Listbox(self.frame, listvariable=self.lnames, height = 5)
        self.nameDisplay = ttk.Label(self.frame, textvariable=self.nameof)
        
        #grids
        self.lbox.grid(column = 0, row = 0, rowspan = 6, sticky = (N,S,E,W))
        self.nameDisplay.grid(column = 1, row = 0, padx = 10, pady = 5)
        
        #event bindings
        self.lbox.bind('<<ListboxSelect>>', self.showDetails)
        
        #alternate coloring
        for i in range(0, len(self.namelist), 2):
            self.lbox.itemconfigure(i, background = "#f0f0ff")
        
    def showDetails(self, *args):
        idxs = self.lbox.curselection()
        if len(idxs) == 1:
            idx = int(idxs[0])
            self.lbox.see(idx)
            name = self.namelist[idx]
            self.nameof.set('Name of Canteen: %s' % (name))
        

def main():
    root = Tk()
    app = startScreen(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
