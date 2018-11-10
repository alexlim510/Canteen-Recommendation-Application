#import json

#with open('canteen.json','r') as f:
    #canteendata = json.load(f)
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

    print("list of booths: ", end='')
    for item in canteen_booth_list:
        print(item[1], end=', ')

    print("list of canteens: ", end='')
    for item in canteen_booth_list:
        print(item[0], end=', ')


def search_by_food(canteendata, user_food):
    canteen_booth_list = get_canteen_booth(canteendata, user_food)
    if canteen_booth_list == []:
        print("No canteen provide this food.")
    else:
        print_canteen_booth(canteen_booth_list)

