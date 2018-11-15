from tkinter import *
from tkinter import ttk
import pygame

class startScreen:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.configure = Button(self.frame, text = "⚙ Configure", command = self.openConfigure)
        self.title = Label(self.frame, text = "Welcome")
        self.locdetail = StringVar(value = "Click here to retrieve your location")
        self.searchLabel = Label(self.frame, text = "Show food outlets based on:")
        self.current_loc = Button(self.frame, textvariable = self.locdetail, command = self.openLocSelector)
        self.sort_dist = Button(self.frame, text = "Distance", command = self.openSortDist)
        self.sort_food = Button(self.frame, text = "Food", command = self.openSortFood)
        self.sort_rank = Button(self.frame, text = "Rank", command = self.openSortRank)
        self.sort_price = Button(self.frame, text = "Price", command = self.openSortPrice)
        
        
        #grid/pack
        self.configure.pack()
        self.current_loc.pack()
        self.searchLabel.pack()
        self.sort_dist.pack()
        self.sort_food.pack()
        self.sort_rank.pack()
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
        self.app = sortedListViewer(self.newWindow) # ,"dist"
        
    def openSortFood(self):
        self.newWindow = Toplevel(self.master)
        self.app = sortedListViewer(self.newWindow) # ,"food"
    
    def openSortRank(self):
        self.newWindow = Toplevel(self.master)
        self.app = sortedListViewer(self.newWindow) # ,"rank"
        
    def openSortPrice(self):
        self.newWindow = Toplevel(self.master)
        self.app = sortedListViewer(self.newWindow) # ,"price"

class sortedListViewer:
    def __init__(self, master): #(self, master, sortby)
        self.master = master
        self.frame = ttk.Frame(self.master) #padding
        self.frame.grid(column = 0, row = 0, sticky = (N,W,E,S))
        self.master.grid_columnconfigure(0, weight = 1)
        self.master.grid_rowconfigure(0, weight = 1)
        
        #variables, LINK FUNCTIONS TO THIS
        #CURRENTLY USED FOR TESTING, CHANGE LATER
        self.namelist = ('Canteen 1', 'Canteen 2', 'Canteen 4', 'Canteen 9')
        self.pricelist = (3.95, 4.33, 2.34, 5.66)
        self.foodlist = ('biryani', 'fish soup', 'chicken rice', 'ramen')
        
        self.lnames = StringVar(value=self.namelist)
        
        self.nameof = StringVar(value="Canteen 2") #test value
        self.rankof = StringVar(value="Rank #5") #test
        self.distof = StringVar(value="800m") #test
        
        #widget
        #do we really need labels?
        self.lbox = Listbox(self.frame, listvariable=self.lnames, height = 5)
#        self.nameLabel = ttk.Label(self.frame, text = "Name: ")
        self.nameDisplay = ttk.Label(self.frame, textvariable=self.nameof)
        self.rankDisplay = ttk.Label(self.frame, textvariable=self.rankof)
        self.distDisplay = ttk.Label(self.frame, textvariable=self.distof)
        
        #Treeview for food varieties and prices
        self.foodPriceDisplay = ttk.Treeview(self.frame, columns = ('Food', 'Price'), show='headings')
        self.foodPriceDisplay.heading('Food', text ='Food')
        self.foodPriceDisplay.heading('Price', text ='Price')
        
        #grids
        self.lbox.grid(column = 0, row = 0, rowspan = 4, sticky = (N,S,E,W))
        self.nameDisplay.grid(column = 1, row = 0, padx = 10, pady = 5)
        self.rankDisplay.grid(column = 1, row = 1, padx = 10, pady = 5)
        self.distDisplay.grid(column = 1, row = 2, padx = 10, pady = 5)
        self.foodPriceDisplay.grid(column = 1, row = 3, padx = 10, pady = 5)
        
        #event bindings
        self.lbox.bind('<<ListboxSelect>>', self.showDetails)
        
        #alternate coloring
        for i in range(0, len(self.namelist), 2):
            self.lbox.itemconfigure(i, background = "#f0f0ff")
        
        #test, need to add to showDetails
        for i in range(0, len(self.foodlist)):
            self.foodPriceDisplay.insert('', 'end', values=(self.foodlist[i], self.pricelist[i]))
        
    def showDetails(self, *args):
        list_index_tup = self.lbox.curselection()
        if len(list_index_tup) == 1:
            indx = int(list_index_tup[0])
            self.lbox.see(indx)
            name = self.namelist[indx]
            self.nameof.set(name)
        

def main():
    root = Tk()
    app = startScreen(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
