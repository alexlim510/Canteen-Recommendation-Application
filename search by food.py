import json
from tkinter import *
############################################################################
#LINEAR SEARCH
def get_canteen_booth(canteendata,user_food):

    canteen_booth_list = []

    for canteen in canteendata['canteen']:
        for booths in canteendata['canteen'][canteen]['booths']:
            for food in canteendata['canteen'][canteen]['booths'][booths]:
                if food == user_food:
                    canteen_booth_list.append((canteen,booths))
    return canteen_booth_list

#multiple booths in canteen
def print_canteen_booth(canteen_booth_list):        
    canteen_list = []
    booth_list = []

    boothlist = "list of booths: "
    for item in canteen_booth_list:
        boothlist = boothlist + ',' + item[1]

    canteenlist = "list of canteens: "
    for item in canteen_booth_list:
        canteenlist = canteenlist + ',' + item[0]

    

def printbooth(canteen_booth_list, root):
    for item in canteen_booth_list:
        Label(root, text = item[0] + ': ' + item[1]).pack()

        

def search_by_food(canteendata, user_food, root):
    canteen_booth_list = get_canteen_booth(canteendata, user_food)
    if canteen_booth_list == []:
        Label(root, text = "No canteen provide this food.").pack()
    else:
        printbooth(canteen_booth_list,root)



