from geopy import distance

def search_by_food(canteendata,user_food):
    added = False
    canteen_list = []
    rank_list=[]
    food_list=[]
    price_list=[]
    gps_list = []

    for canteen in canteendata['canteen']:
        for booths in canteendata['canteen'][canteen]['booths']:
            for food in canteendata['canteen'][canteen]['booths'][booths]:
                price = canteendata['canteen'][canteen]['booths'][booths][food]
                rank = canteendata['canteen'][canteen]['rank']
                gps = canteendata['canteen'][canteen]['gps coordinates']
                if user_food in food:
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
                        gps_list.append(canteendata['canteen'][canteen]['gps coordinates'])
                    added = False
    return canteen_list, rank_list, food_list, price_list, gps_list
    
def search_by_price(canteendata,max_price):
    canteen_list = []
    rank_list = []
    food_list = []
    price_list = []
    gps_list = []
    added = False

    for canteen in canteendata['canteen']:
        for booths in canteendata['canteen'][canteen]['booths']:
            for food in canteendata['canteen'][canteen]['booths'][booths]:
                price = canteendata['canteen'][canteen]['booths'][booths][food]
                rank = canteendata['canteen'][canteen]['rank']
                gps = canteendata['canteen'][canteen]['gps coordinates']
                if canteendata['canteen'][canteen]['booths'][booths][food] <= max_price:
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
                        gps_list.append(canteendata['canteen'][canteen]['gps coordinates'])                        
                    added = False                    
    return canteen_list, rank_list, food_list, price_list, gps_list
    
def calc_dist_multiple_gps(current_loc, gps_data):
    #current_loc is a tuple/list with latlong of current location
    #gps_data is a tuple/list of latlongs
    dist_list = []
    for i in gps_data:
        dist_list.append(distance.distance(current_loc, i).m)
    return dist_list
    