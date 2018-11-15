import json

with open('canteen.json','r') as f:
    canteendata = json.load(f)


##############################################################################################################
#PRICE RANGE AS TUPLE e.g.(0, 4.00)
#LINEAR SEARCH

def get_canteen_booth(canteendata,price_range):
    canteen_list = []
    rank_list = []
    food_list = []
    price_list = []
    added = False

    for canteen in canteendata['canteen']:
        for booths in canteendata['canteen'][canteen]['booths']:
            for food in canteendata['canteen'][canteen]['booths'][booths]:
                price = canteendata['canteen'][canteen]['booths'][booths][food]
                rank = canteendata['canteen'][canteen]['rank']
                if price_range[0] <= canteendata['canteen'][canteen]['booths'][booths][food] <= price_range[1]:
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


def search_by_price(canteendata, price_range):
    canteen_list, rank_list, food_list, price_list = get_canteen_booth(canteendata, price_range)
    return canteen_list, rank_list, food_list, price_list
        

