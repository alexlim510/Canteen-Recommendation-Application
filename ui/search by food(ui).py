import json
from tkinter import *

with open("canteen.json", 'r') as f:
    canteendata = json.load(f)
############################################################################
#LINEAR SEARCH
#search_by_food(canteendata, user_food)
#variables = canteen_list, rank_list, food_list, price_list


def get_canteen_booth(canteendata,user_food):
    added = False
    canteen_list = []
    rank_list=[]
    food_list=[]
    price_list=[]

    for canteen in canteendata['canteen']:
        for booths in canteendata['canteen'][canteen]['booths']:
            for food in canteendata['canteen'][canteen]['booths'][booths]:
                price = canteendata['canteen'][canteen]['booths'][booths][food]
                rank = canteendata['canteen'][canteen]['rank']
                if food == user_food:
                    for item in canteen_list:
                        if item == canteen:
                            food_list[canteen_list.index(canteen)].append(food)
                            price_list[canteen_list.index(canteen)].append(price)
                            added = True
                            break
                    if added == False:
                        canteen_list.append(canteen)
                        rank_list.append(canteendata['canteen'][canteen]['rank'])
                        food_list.append([food])
                        price_list.append([price])
                    added = False
    return canteen_list, rank_list, food_list, price_list

        
def search_by_food(canteendata, user_food):
    canteen_list, rank_list, food_list, price_list = get_canteen_booth(canteendata, user_food)
    return canteen_list, rank_list, food_list, price_list


