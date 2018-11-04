import json


#Split into 2 major parts
# 1) Add or Change data
# 2) Remove data
###################################################################################################################################################
#functions for add or change data


def introduction_add_or_change():
    print("What would you like to update?")
    print("1) Add canteens")
    print("2) Add booths")
    print("3) Add food")
    print("4) Change price")
    print("5) Add/change address")
    print("6) Add/change canteen rank")
    

#check if canteen exists
def check_canteen(canteendata, canteen):
    exist = False
    for existing_canteen in canteendata['canteen']:
        if canteen == existing_canteen:
            exist = True
    return exist


#retrieve canteen
def obtain_canteen(canteendata):
    obtained_canteens = []
    print("please input canteens. If done, input done")
    while True:
        obtained_canteen = input("Please input canteen: ")
        if obtained_canteen == "done":
            break
        elif obtained_canteen == "":
            print("Please input a canteen.")
        else:
            for item in obtained_canteens:
                    if obtained_canteen == item:
                        print("You have inputted this canteen.")
                        continue
            if any(canteendata['canteen'].values()): #check if there is any canteen. if not, add canteen without checking existence 
                if check_canteen(canteendata,obtained_canteen):   # check for existence of canteen, otherwise may overwrite existing canteen
                    print("This canteen exists. ")
                    continue
                else:
                    obtained_canteens.append(obtained_canteen)
            else:
                obtained_canteens.append(obtained_canteen)
    return obtained_canteens


#check if booth exist
def check_booth(canteendata, canteen, booth):
    exist = False
    for existing_booths in canteendata['canteen'][canteen]['booths']: #check for existence of booth, otherwise may overwrite existing booth
        if booth == existing_booths:
            exist = True
            break
    return exist


#retrieve and check booth
def obtain_booth(canteendata, canteen):
    obtained_booths = []
    print("please input booths. If done, input done")
    while True:
            obtained_booth = input("Please input booth: ")
            if obtained_booth == "done":
                break
            elif obtained_booth == "":
                print("Please input a booth.")
            else:
                for item in obtained_booths:
                    if obtained_booth == item:
                        print("You have inputted this booth.")
                        continue
                if any(canteendata['canteen'][canteen]['booths'].values()): #check if canteen has value. if not, add booth to canteen without checking existence 
                    if check_booth(canteendata, canteen, obtained_booth):
                        print ("This booth exists. ")
                        continue
                    else:
                        obtained_booths.append(obtained_booth)
                else:
                    obtained_booths.append(obtained_booth)
    return obtained_booths
                    

#check if food exists
def check_food(canteendata, canteen, booth, food):
    exist = False
    for existing_food in canteendata['canteen'][canteen]['booths'][booth]: #check for existence of food, otherwise may overwrite existing food
        if existing_food == food:
            exist = True
            break
    return exist


#retrieve and check food and price
def obtain_food_and_price(canteendata, canteen, booth):
    food_and_price = []
    obtained_price = 0
    print("please input food and price. If done, input done")
    while True:
            obtained_food = input("Please input food: ")
            if obtained_food == "done" or obtained_price == "done":
                break
            elif obtained_food == "":
                print ("Please input a food.")
            else:
                for item in food_and_price:
                    if obtained_food == item:
                        print("You have inputted this food.")
                        continue
                if any(canteendata['canteen'][canteen]['booths'][booth].values()):
                    if check_food(canteendata, canteen, booth, obtained_food): #check if food exist in database
                        print("This food exist in the booth ", booth, ".")
                        continue
                    else:
                        while True:
                            obtained_price = input("Please input price: ")
                            if obtained_price == "done":
                                break
                            elif obtained_price == "":
                                print ("Please input a price.")
                            else:
                                food_and_price.append((obtained_food, obtained_price))
                                break
                else:
                    while True:
                        obtained_price = input("Please input price: ")
                        if obtained_price == "done":
                            break
                        elif obtained_price == "": 
                            print ("Please input a price.")
                        else:
                            food_and_price.append((obtained_food, obtained_price))
                            break
    return food_and_price #food and price as list of tuples    


#retrieve price
def obtain_price():
    while True:
        obtained_price = input("please input price: ")
        if obtained_price == "":
            print("Please input a price.")
        else:
            return obtained_price
    

#retrieve address
def obtain_address():
    while True:
        obtained_address = input("Please input address: ")
        if obtained_address == "":
            print("Please input an address.")
        else:
            return obtained_address


#retrieve canteen rank
def obtain_rank():
    while True:
        obtained_rank = input("Please input rank: ")
        if obtained_rank == "":
            print("Please input a rank.") 
        else:
            return obtained_rank


#Adding canteen
def add_canteen (canteendata, canteen):
    for new_canteens in canteen:
            canteendata['canteen'][new_canteens] = {}
            canteendata['canteen'][new_canteens]["address"] = None
            canteendata['canteen'][new_canteens]["booths"] = {}
            canteendata['canteen'][new_canteens]["rank"] = None
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


#Adding booth
def add_booth (canteendata, canteen, booth):
    for new_booths in booth:
            canteendata['canteen'][canteen]["booths"][new_booths] = {}
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


#Adding food and price
def add_food (canteendata, canteen, booth, food_and_price):
    for new_food in food_and_price:
        canteendata['canteen'][canteen]["booths"][booth][new_food[0]] = new_food[1]
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


#Change price
def change_price(canteendata, canteen, booth, food, price):
    canteendata['canteen'][canteen]["booths"][booth][food] = price
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


#update address
def change_address (canteendata, canteen, address):
    canteendata['canteen'][canteen]["address"] = address
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


#update rank
def change_rank (canteendata, canteen, rank):
    canteendata['canteen'][canteen]["rank"] = rank
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)
###############################################################
#functions for remove data


def introduction_remove():
    print("What would you like to remove?")
    print("1) Remove canteens")
    print("2) Remove booths")
    print("3) Remove food")


#obtain canteen to remove
def obtain_canteen_to_remove(canteendata):
    obtained_canteens = []
    print("please input canteen. If done, input done")
    while True:
            obtained_canteen = input("Please input canteen to remove: ")
            if obtained_canteen == "done":
                break
            elif obtained_canteen == "":
                print("Please input a booth.")
            else:
                for item in obtained_canteens:
                    if obtained_canteen == item:
                        print("You have inputted this booth.")
                        continue
                if check_canteen(canteendata, obtained_canteen):
                    obtained_canteens.append(obtained_canteen)
                else:
                    print("Please input a valid canteen")
    return obtained_canteens

#remove canteen
def remove_canteen(canteendata, canteen):
    for existing_canteen in canteen:
        del canteendata['canteen'][existing_canteen]
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


#obtain booth to remove
def obtain_booth_to_remove(canteendata, canteen):
    obtained_booths = []
    print("please input booths. If done, input done")
    while True:
            obtained_booth = input("Please input booth to remove: ")
            if obtained_booth == "done":
                break
            elif obtained_booth == "":
                print("Please input a booth.")
            else:
                for item in obtained_booths:
                    if obtained_booth == item:
                        print("You have inputted this booth.")
                        continue
                if check_booth(canteendata, canteen, obtained_booth):
                    obtained_booths.append(obtained_booth)
                else:
                    print("Please input a valid booth")
    return obtained_booths

#remove booth
def remove_booth(canteendata, canteen, booth):
    for existing_booth in booth:
        del canteendata['canteen'][canteen]["booths"][existing_booth]
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


#obtain food to remove
def obtain_food_to_remove(canteendata, canteen, booth):
    obtained_foods = []
    print("please input food. If done, input done")
    while True:
            obtained_food = input("Please input food to remove: ")
            if obtained_food == "done":
                break
            elif obtained_food == "":
                print("Please input a food.")
            else:
                for item in obtained_food:
                    if obtained_food == item:
                        print("You have inputted this food.")
                        continue
                if check_food(canteendata, canteen, booth, obtained_food):
                    obtained_foods.append(obtained_food)
                else:
                    print("Please input a valid food")
    return obtained_foods

#remove food
def remove_food(canteendata, canteen, booth, food):
    for existing_food in food:
        del canteendata['canteen'][canteen]["booths"][booth][existing_food]
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


################################################################
#Add or change canteen data function


def add_or_change_data(canteendata):
    while True:
        try:
            introduction_add_or_change()
            choice = int(input())
            complete = False


        except:
            print("Please input a valid number ")


        else:
            if choice == 1: #add or change canteen
                canteen = obtain_canteen(canteendata)
                add_canteen(canteendata, canteen)
                print("done")
                #break
        

            elif choice == 2: #add or change booth
                while not complete:
                    canteen = input("Please input canteen: ")
                    if check_canteen(canteendata, canteen):
                        booth = obtain_booth(canteendata, canteen)
                        add_booth(canteendata, canteen, booth)
                        print("done")
                        complete = True
                    else:    
                        print ("Please input valid canteen.")
                #break


            elif choice == 3: #add or change food
                while not complete:
                    canteen = input("Please input canteen: ")
                    if check_canteen(canteendata, canteen):
                        while not complete:
                            booth = input("Please input booth: ")
                            if check_booth(canteendata, canteen, booth):
                                food_and_price = obtain_food_and_price(canteendata, canteen, booth)
                                add_food(canteendata, canteen, booth, food_and_price)
                                print("done")
                                complete = True
                            else:    
                                print("Please input valid booth.")
                    else:
                        print("Please input valid canteen.")
                #break

            elif choice == 4: #add or change price
                while not complete:
                    canteen = input("Please input canteen: ")
                    if check_canteen(canteendata, canteen):
                        while not complete:
                            booth = input("Please input booth: ")
                            if check_booth(canteendata, canteen, booth):
                                while not complete:
                                    food = input("Please input food: ")
                                    if check_food(canteendata, canteen, booth, food):
                                        price = obtain_price()
                                        change_price(canteendata, canteen, booth, food, price)
                                        print("done")
                                        complete = True
                                    else:
                                        print("Please input a valid food. ")
                            else:    
                                print("Please input valid booth.")
                    else:
                        print("Please input valid canteen.")
                #break


            elif choice == 5: #add or change address
                while not complete:
                    canteen = input("Please input canteen: ")
                    if check_canteen(canteendata, canteen):
                        address = obtain_address()
                        change_address (canteendata, canteen, address)
                        print("done")
                        complete = True
                    else:
                        print ("Please input valid canteen.")
                #break

            elif choice == 6: #add or change rank
                while not complete:
                    canteen = input("Please input canteen: ")
                    if check_canteen(canteendata, canteen):
                        rank = obtain_rank()
                        change_rank (canteendata, canteen, rank)
                        print("done")
                        complete = True
                    else:
                        print ("Please input valid canteen.")
                #break
            
            else:
                print ("Please input 1, 2, 3, 4, 5.")

            
#############################################################################################################
#Remove data function


def remove_data(canteendata):
    while True:
        try:
            introduction_remove()
            choice = int(input())
            complete = False


        except:
            print("Please input a valid number ")


        else:
            if choice == 1: #remove canteen
                if any(canteendata['canteen'].values()):
                    canteen = obtain_canteen_to_remove(canteendata)
                    remove_canteen(canteendata, canteen)
                    print("done")
                else:
                    print("There is no canteen.")
                    #break
        

            elif choice == 2: #remove booth
                if any(canteendata['canteen'].values()):
                    while not complete:
                        canteen = input("Please input canteen: ")
                        if check_canteen(canteendata, canteen):
                            if any(canteendata['canteen'][canteen]['booths'].values()):
                                booth = obtain_booth_to_remove(canteendata, canteen)
                                remove_booth(canteendata, canteen, booth)
                                print("done")
                                complete = True
                            else:
                                print("There is no booth.")
                                break
                        else:    
                            print ("Please input valid canteen.")
                else:
                    print("There is no canteen.")
                #break


            elif choice == 3: #remove food
                if any(canteendata['canteen'].values()):
                    while not complete:
                        canteen = input("Please input canteen: ")
                        if check_canteen(canteendata, canteen):
                            if any(canteendata['canteen'][canteen]['booths'].values()):
                                while not complete:
                                    booth = input("Please input booth: ")
                                    if check_booth(canteendata, canteen, booth):
                                        if any(canteendata['canteen'][canteen]['booths'][booth].values()):
                                            food = obtain_food_to_remove(canteendata, canteen, booth)
                                            remove_food(canteendata, canteen, booth, food)
                                            print("done")
                                            complete = True
                                        else:
                                            print("There is no food.")
                                            complete = True
                                    else:    
                                        print("Please input valid booth.")
                            else:
                                print("There is no booth.")
                                complete = True
                        else:
                            print("Please input valid canteen.")
                else:
                    print("There is no canteen.")
##############################################################################################################
#Functions for update data


def introduction_update():
    print("How would you like to update?")
    print("1) Add or change")
    print("2) Remove")



def update_data(canteendata):
    while True:
        try:
            introduction_update()
            choice = int(input())


        except:
            print("Please input a valid number ")


        else:
            if choice == 1:
                add_or_change_data(canteendata)

            if choice == 2:
                remove_data(canteendata)

#############################################################################################################
#Opens json file 
with open('canteen.json', 'r') as f:
    canteendata = json.load(f)

update_data(canteendata)



        









