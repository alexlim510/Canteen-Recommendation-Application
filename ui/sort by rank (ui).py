import json

with open('canteen.json','r') as f:
    canteendata = json.load(f)

##############################################################
#canteenrank_list = [(canteen a, 1),(canteen b, 2).....]
#MERGE SORT
def merge(canteen_list_left , canteen_list_right):
    merge_canteen_list = []

    while canteen_list_left  and canteen_list_right:
        if canteen_list_left[0][1] < canteen_list_right[0][1]:
            merge_canteen_list.append(canteen_list_left[0])
            canteen_list_left.pop(0)
        else:
            merge_canteen_list.append(canteen_list_right[0])
            canteen_list_right.pop(0)

    if canteen_list_left:
        merge_canteen_list.extend(canteen_list_left)
    else:
        merge_canteen_list.extend(canteen_list_right)

    return merge_canteen_list
        


def mergesort(canteen_list):
    length_list = len(canteen_list)

    if length_list <= 1:
        return canteen_list

    canteen_list_left = canteen_list[:length_list // 2]
    canteen_list_right = canteen_list[length_list // 2:] 

    canteen_list_left = mergesort(canteen_list_left)
    canteen_list_right  = mergesort(canteen_list_right)

    return merge(canteen_list_left , canteen_list_right)

#####################################################################################
#canteenrank_list = [(canteen a, 1),(canteen b, 2).....]
def sort_by_rank(canteendata):
    canteenrank_list = []
    canteen_list = []
    rank_list = []
    food_list = []
    price_list = []
    gps_list = []
    added = False
    
    for canteens in canteendata['canteen']:
        canteenrank_list.append((canteens, canteendata['canteen'][canteens]['rank']))
    print(canteenrank_list)
    print('test')
    canteenrank_list = mergesort(canteenrank_list)
    print('AAAAA')
    print(canteenrank_list)
    
    for item in canteenrank_list:
        for booths in canteendata['canteen'][item[0]]['booths']:
            for food in canteendata['canteen'][item[0]]['booths'][booths]:
                price = canteendata['canteen'][item[0]]['booths'][booths][food]
                for itemc in canteen_list:
                     if itemc == item[0]:
                         food_list[canteen_list.index(item[0])].append(food)
                         price_list[canteen_list.index(item[0])].append(price)
                         added = True
                         break
                if added == False:
                    canteen_list.append(item[0])
                    rank_list.append(item[1])
                    food_list.append([food])
                    price_list.append([price])
                    gps_list.append(canteendata['canteen'][item[0]]['gps coordinates'])
                added = False
    return canteen_list, rank_list, food_list, price_list, gps_list

