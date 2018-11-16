from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import pygame
import json
from helper import *
from sort_by_distance import *
from web_scrapper import *

current_loc = None

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
        pygame.init()

        # take this to be top left point
        hall_12_bus_stop_coordinates = (1.351937, 103.680543)
        hall_12_pixel_coordinates = (317, 503) # when scale = 3

        # take this to be bottom right point
        hall_1_bus_stop_coordinates = (1.345645, 103.687804)
        hall_1_pixel_coordinates = (799, 926) # when scale = 3

        difference_in_pixels = (hall_1_pixel_coordinates[0] - hall_12_pixel_coordinates[0], hall_1_pixel_coordinates[1] - hall_12_pixel_coordinates[1])
        difference_in_coordinates = (hall_1_bus_stop_coordinates[0] - hall_12_bus_stop_coordinates[0], hall_1_bus_stop_coordinates[1] - hall_12_bus_stop_coordinates[1])

        map = pygame.image.load('map.png')
        scale = 3 # used to scale the image
        display_width = round(map.get_width() / scale)
        display_height = round(map.get_height() / scale)
        screen = pygame.display.set_mode([display_width,display_height])

        scaled_map = pygame.transform.scale(map, (display_width, display_height))

        click = (0, 0)

        def event_handler():
            for event in pygame.event.get():
                #print(event) # this prints all the events detected by pygame.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #quit() # stop python program execution 
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = pygame.mouse.get_pos()
                    #print(click)
                    #print(difference_in_pixels)
                    ratio = ((click[0]-hall_12_pixel_coordinates[0])/difference_in_pixels[0], (click[1]-hall_12_pixel_coordinates[1])/difference_in_pixels[1])
                    #print(ratio)
                    new_coordinates = (hall_12_bus_stop_coordinates[0]+difference_in_coordinates[0]*ratio[1], hall_12_bus_stop_coordinates[1]+difference_in_coordinates[1]*ratio[0])
                    # print(new_coordinates)
                    return new_coordinates

        game_running = True

        while game_running:
            output = event_handler()
            #print(output)
            screen.blit(scaled_map, (0, 0))
            pygame.display.flip()
            if output != None:
                global current_loc
                current_loc = output
                game_running = False
                pygame.quit()
                #print(current_loc)
    
    def openSortDist(self):
        if current_loc == None:
            messagebox.showinfo("Error", "Please select your current location before continuing.")
        else:
            with open("canteen.json", 'r') as f:
                canteendata = json.load(f)
            self.data = sort_by_rank(canteendata)
            self.namelist, self.ranklist, self.foodlist, self.pricelist, self.distlist, self.gpslist = self.data[0], self.data[1], self.data[2], self.data[3], calc_dist_multiple_gps(current_loc, self.data[4]), self.data[4] 
            self.zipped = list(zip(self.distlist, self.namelist, self.ranklist, self.foodlist, self.pricelist, self.gpslist))
            self.zipped.sort()
            self.distlist, self.namelist, self.ranklist, self.foodlist, self.pricelist, self.gpslist = zip(*self.zipped)
            self.newWindow = Toplevel(self.master)
            self.app = sortedListViewer(self.newWindow, self.namelist, self.pricelist, self.ranklist, self.foodlist, self.distlist, self.gpslist)
    
    def openSortRank(self):
        if current_loc == None:
            messagebox.showinfo("Error", "Please select your current location before continuing.")
        else:
            with open("canteen.json", 'r') as f:
                canteendata = json.load(f)
            self.data = sort_by_rank(canteendata)
            self.namelist, self.ranklist, self.foodlist, self.pricelist, self.distlist = self.data[0], self.data[1], self.data[2], self.data[3], calc_dist_multiple_gps(current_loc, self.data[4]) 
            self.gpslist = self.data[4]
            self.newWindow = Toplevel(self.master)
            self.app = sortedListViewer(self.newWindow, self.namelist, self.pricelist, self.ranklist, self.foodlist, self.distlist, self.gpslist)
        
    def openSortFood(self):
        if current_loc == None:
            messagebox.showinfo("Error", "Please select your current location before continuing.")
        else:
            self.foodsearch = simpledialog.askstring("Sort by Food", "Enter the type of food you would like to search:")
            if self.foodsearch == None:
                messagebox.showinfo("Error", "Please enter a valid food type.")
            else:
                with open("canteen.json", 'r') as f:
                    canteendata = json.load(f)
                self.data = search_by_food(canteendata,self.foodsearch)
                self.namelist, self.ranklist, self.foodlist, self.pricelist, self.distlist = self.data[0], self.data[1], self.data[2], self.data[3], calc_dist_multiple_gps(current_loc, self.data[4]) 
                self.gpslist = self.data[4]
                self.newWindow = Toplevel(self.master)
                self.app = sortedListViewer(self.newWindow, self.namelist, self.pricelist, self.ranklist, self.foodlist, self.distlist, self.gpslist)
                    
    def openSortPrice(self):
        if current_loc == None:
            messagebox.showinfo("Error", "Please select your current location before continuing.")
        else:
            self.maxprice = simpledialog.askfloat("Sort by Price", "Enter the maximum price of food you would like to search:")
            if self.maxprice == None:
                messagebox.showinfo("Error", "Please enter a valid amount")
            else:
                with open("canteen.json", 'r') as f:
                    canteendata = json.load(f)
                self.data = search_by_price(canteendata,self.maxprice)
                self.namelist, self.ranklist, self.foodlist, self.pricelist, self.distlist = self.data[0], self.data[1], self.data[2], self.data[3], calc_dist_multiple_gps(current_loc, self.data[4])
                self.gpslist = self.data[4]
                self.newWindow = Toplevel(self.master)
                self.app = sortedListViewer(self.newWindow, self.namelist, self.pricelist, self.ranklist, self.foodlist, self.distlist, self.gpslist)

class sortedListViewer:
    def __init__(self, master, namelist, pricelist, ranklist, foodlist, distlist, gpslist):
        self.master = master
        self.frame = ttk.Frame(self.master) #padding
        self.frame.grid(column = 0, row = 0, sticky = (N,W,E,S))
        self.master.grid_columnconfigure(0, weight = 1)
        self.master.grid_rowconfigure(0, weight = 1)

        self.namelist = namelist
        self.pricelist = pricelist
        self.ranklist = ranklist
        self.foodlist = foodlist
        self.distlist = distlist
        self.gpslist = gpslist
        
        #variables
        self.lnames = StringVar(value=self.namelist)        
        self.nameof = StringVar()
        self.rankof = StringVar()
        self.distof = StringVar()
        self.walking = StringVar(value="Walk")
        self.bussing = StringVar(value="Bus+Walk")
        
        #widget
        #do we need labels?
        self.lbox = Listbox(self.frame, listvariable=self.lnames, height = 5)
        self.nameDisplay = ttk.Label(self.frame, textvariable=self.nameof)
        self.rankDisplay = ttk.Label(self.frame, textvariable=self.rankof)
        self.distDisplay = ttk.Label(self.frame, textvariable=self.distof)
        self.naviWalk = ttk.Button(self.frame, textvariable = self.walking, command=self.openWalkingDirections)
        self.naviBus = ttk.Button(self.frame, textvariable = self.bussing, command=self.openBusDirections)
        
        #Treeview for food varieties and prices
        self.foodPriceDisplay = ttk.Treeview(self.frame, columns = ('Food', 'Price'), show='headings')
        self.foodPriceDisplay.heading('Food', text ='Food')
        self.foodPriceDisplay.heading('Price', text ='Price')
        
        #grids
        self.lbox.grid(column = 0, row = 0, rowspan = 4, padx = 10, pady = 5, sticky = (N,S,E,W))
        self.nameDisplay.grid(column = 1, row = 0, padx = 10, pady = 5)
        self.rankDisplay.grid(column = 1, row = 1, padx = 10, pady = 5)
        self.distDisplay.grid(column = 1, row = 2, padx = 10, pady = 5)
        self.naviWalk.grid(column = 1, row = 3, padx = 10, pady = 5)
        self.naviBus.grid(column = 1, row = 4, padx = 10, pady = 5)
        self.foodPriceDisplay.grid(column = 1, row = 5, padx = 10, pady = 5)
        
        #event bindings
        self.lbox.bind('<<ListboxSelect>>', self.showDetails)
        
        #alternate coloring
        for i in range(0, len(self.namelist), 2):
            self.lbox.itemconfigure(i, background = "#f0f0ff")
        
    def showDetails(self, *args):
        #assume all datasets are sorted accordingly
        #common sets share the same index
        #tuples of tuples - food and prices
        lbox_index_tup = self.lbox.curselection()
        if len(lbox_index_tup) == 1:
            indx = int(lbox_index_tup[0])
            self.lbox.see(indx) #change focus
            self.nameof.set("Name: %s" % self.namelist[indx])
            self.rankof.set("Rank: #%i" % self.ranklist[indx])
            self.distof.set("Distance from current location: %fm" % self.distlist[indx])
            #clear treeview
            self.foodPriceDisplay.delete(*self.foodPriceDisplay.get_children())
            for i in range(0, len(self.foodlist[indx])):
                self.foodPriceDisplay.insert('', 'end', values = (self.foodlist[indx][i], self.pricelist[indx][i]))
    
    def openWalkingDirections(self):
        lbox_index_tup = self.lbox.curselection()
        if len(lbox_index_tup) == 0:
            messagebox.showinfo("Error", "Please select a location")
        else:
            indx = int(lbox_index_tup[0])
            self.lbox.see(indx)
            self.dest_loc = self.gpslist[indx]
            self.newWindow = Toplevel(self.master)
            self.app = walkingDirectionViewer(self.newWindow, current_loc, self.dest_loc)
    
    def openBusDirections(self):
        lbox_index_tup = self.lbox.curselection()
        if len(lbox_index_tup) == 0:
            messagebox.showinfo("Error", "Please select a location")
        else:
            indx = int(lbox_index_tup[0])
            self.lbox.see(indx)
            self.dest_loc = self.gpslist[indx]
            self.newWindow = Toplevel(self.master)
            self.app = busDirectionViewer(self.newWindow, current_loc, self.dest_loc)
    
class walkingDirectionViewer:
    def __init__(self, master, current_loc, dest_loc):
        self.master = master
        self.frame = ttk.Frame(self.master) #padding
        self.frame.grid(column = 0, row = 0, sticky = (N,W,E,S))
        self.master.grid_columnconfigure(0, weight = 1)
        self.master.grid_rowconfigure(0, weight = 1)
        
        self.current_loc = current_loc
        self.dest_loc = dest_loc
        self.webadd = convert_coordinates_walking_html2(current_loc, dest_loc)
        a = walking_directions(self.webadd)
        
        self.directions = a.get_directions_directions()
        self.traveltime = a.get_total_time()
        self.totaldist = a.get_total_distance()
        print(self.totaldist)
        self.ldir = StringVar(value = self.directions)
        self.ttime = StringVar(value = self.traveltime)
        self.tdist = StringVar(value = self.totaldist)
        
        self.titlelabel = Label(self.frame, text="Walking Directions")
        self.disttaken = Label(self.frame, textvariable=self.tdist)
        self.timetaken = Label(self.frame, textvariable=self.ttime)
        self.lbox = Listbox(self.frame, listvariable=self.ldir, height = 20, width = 50)
        
        self.titlelabel.grid(column = 0, row = 0, padx = 10, pady = 5)
        self.disttaken.grid(column = 1, row = 0, padx = 10, pady = 5)
        self.timetaken.grid(column = 1, row = 1, padx = 10, pady = 5)
        self.lbox.grid(column = 0, row = 1, rowspan = 4, padx = 10, pady = 5, sticky = (N,S,E,W))

class busDirectionViewer:
    def __init__(self, master, current_loc, dest_loc):
        self.master = master
        self.frame = ttk.Frame(self.master) #padding
        self.frame.grid(column = 0, row = 0, sticky = (N,W,E,S))
        self.master.grid_columnconfigure(0, weight = 1)
        self.master.grid_rowconfigure(0, weight = 1)
        
        self.current_loc = current_loc
        self.dest_loc = dest_loc
        self.webadd = convert_coordinates_bus_html2(current_loc, dest_loc)[0]
        b = bus_directions(self.webadd)
        
        self.directions = b.get_directions_directions()
        self.traveltime = b.get_total_time()
        self.totaldist = b.get_directions_distance()
        print(self.totaldist)
        self.ldir = StringVar(value = self.directions)
        self.ttime = StringVar(value = self.traveltime)
        self.tdist = StringVar(value = self.totaldist)
        
        self.titlelabel = Label(self.frame, text="Bus & Walking Directions")
        self.disttaken = Label(self.frame, textvariable=self.tdist)
        self.timetaken = Label(self.frame, textvariable=self.ttime)
        self.lbox = Listbox(self.frame, listvariable=self.ldir, height = 20, width = 100)
        
        self.titlelabel.grid(column = 0, row = 0, padx = 10, pady = 5)
        self.disttaken.grid(column = 0, row = 2, padx = 10, pady = 5)
        self.timetaken.grid(column = 0, row = 3, padx = 10, pady = 5)
        self.lbox.grid(column = 0, row = 1, rowspan = 4, padx = 10, pady = 5, sticky = (N,S,E,W))

def main():
    root = Tk()
    app = startScreen(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
