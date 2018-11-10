#import json

#with open('canteen.json','r') as f:
    #canteendata = json.load(f)


##############################################################################################################
#PRICE RANGE AS TUPLE e.g.(0, 4.00)
#LINEAR SEARCH

def get_canteen_booth(canteendata,price_range):

    canteen_booth_food_list = []

    for canteen in canteendata['canteen']:
        for booths in canteendata['canteen'][canteen]['booths']:
            for food in canteendata['canteen'][canteen]['booths'][booths]:
                if price_range[0] <= canteendata['canteen'][canteen]['booths'][booths][food] <= price_range[1] :
                    canteen_booth_food_list.append((canteen, booths, food))
    return canteen_booth_food_list


def print_canteen_booth(canteen_booth_food_list):        
    canteen_list = []
    booth_list = []
    food_list = []

    print("list of food: ", end='')
    for item in canteen_booth_food_list:
        print(item[2], end=', ')

    print("list of booths: ", end='')
    for item in canteen_booth_food_list:
        print(item[1], end=', ')

    print("list of canteens: ", end='')
    for item in canteen_booth_food_list:
        print(item[0], end=', ')


def search_by_food(canteendata, price_range):
    canteen_booth_food_list = get_canteen_booth(canteendata, price_range)
    if canteen_booth_food_list == []:
        print("No canteen provide food within this price range.")
    else:
        print_canteen_booth(canteen_booth_food_list)
        

#search_by_food(canteendata, (0,4))