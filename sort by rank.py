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
    for canteens in canteendata['canteen']:
        canteenrank_list.append((canteens, canteendata['canteen'][canteens]['rank']))
    return mergesort(canteenrank_list)

print(sort_by_rank(canteendata))

