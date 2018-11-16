import json
from tkinter import *

#Split into 2 major parts
# 1) Add or Change data
# 2) Remove data
###################################################################################################################################################
#functions for add or change data

def raise_frame(frame):
    frame.tkraise()

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
def obtain_canteen(canteendata, canteen):
    canteen = canteen.get()
    ac_f2 = Toplevel()
    msg_ac = StringVar()
    Label(ac_f2, textvariable = msg_ac).pack()
    if check_canteen(canteendata, canteen):
        msg_ac.set("This canteen exists.")
    else:
        msg_ac.set("Done!")
        add_canteen_a(canteendata, canteen)
        


#check if booth exist
def check_booth(canteendata, canteen, booth):
    exist = False
    for existing_booths in canteendata['canteen'][canteen]['booths']: #check for existence of booth, otherwise may overwrite existing booth
        if booth == existing_booths:
            exist = True
            break
    return exist


#retrieve and check booth
def obtain_booth(canteendata, canteen, booth):
    booth = booth.get()
    ab_f3 = Toplevel()
    msg_ab2 = StringVar()
    Label(ab_f3, textvariable = msg_ab2).pack()
    if check_booth(canteendata, canteen, booth):
        msg_ab2.set("This booth exists.")
    else:
        msg_ab2.set("Done!")
        add_booth_a(canteendata, canteen, booth)

#check if food exists
def check_food(canteendata, canteen, booth, food):
    exist = False
    for existing_food in canteendata['canteen'][canteen]['booths'][booth]: #check for existence of food, otherwise may overwrite existing food
        if existing_food == food:
            exist = True
            break
    return exist


#retrieve and check food and price
def obtain_food_and_price_a(canteendata, canteen, booth, food, price):
    price = price.get()
    af_f5 = Toplevel()
    msg_af5 = StringVar()
    Label(af_f5, textvariable = msg_af5).pack()
    try:
        price = float(price)
        if price <= 0:
            msg_af5.set("Please input a valid price.")
            return None
    except ValueError:
        msg_af5.set("Please input a valid price.") 
    else:
        msg_af5.set("Done!")
        add_food_a(canteendata, canteen, booth, food, price)


def obtain_food_and_price_ca(canteendata, canteen, booth, food, price):
    price = price.get()
    cp_f5 = Toplevel()
    msg_cp5 = StringVar()
    Label(cp_f5, textvariable = msg_cp5).pack()
    try:
        price = float(price)
        if price <= 0:
            msg_cp5.set("Please input a valid price.")
            return None
    except ValueError:
        msg_cp5.set("Please input a valid price.") 
    else:
        msg_cp5.set("Done!")
        change_price_a(canteendata, canteen, booth, food, price)


#retrieve price
def obtain_price():
    while True:
        obtained_price = input("please input price: ")
        if obtained_price == "":
            print("Please input a price.")
        else:
            return obtained_price


def obtain_address_a(canteendata, canteen, address):
    address = address.get()
    aa_f3 = Toplevel()
    Label(aa_f3, text= "Done").pack()
    change_address(canteendata, canteen, address)


#retrieve canteen rank
def obtain_rank_a(canteendata, canteen, rank):
    rank = rank.get()
    ar_f3 = Toplevel()
    Label(ar_f3, text= "Done").pack()
    change_rank(canteendata, canteen, rank)




#Adding canteen
def add_canteen_a (canteendata, canteen):
    canteendata['canteen'][canteen] = {}
    canteendata['canteen'][canteen]["address"] = None
    canteendata['canteen'][canteen]["booths"] = {}
    canteendata['canteen'][canteen]["rank"] = None
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


#Adding booth
def add_booth_a (canteendata, canteen, booth):
    canteendata['canteen'][canteen]["booths"][booth] = {}
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


#Adding food and price
def add_food_a (canteendata, canteen, booth, food, price):
    canteendata['canteen'][canteen]["booths"][booth][food] = price
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


#Change price
def change_price_a(canteendata, canteen, booth, food, price):
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
def obtain_canteen_to_remove(canteendata, canteen):
    canteen = canteen.get()
    rc_f2 = Toplevel()
    msg_rc = StringVar()
    Label(rc_f2, textvariable = msg_rc).pack()
    if check_canteen(canteendata, canteen):
        remove_canteen_a(canteendata,canteen)
        msg_rc.set("Done!")
    else:
        msg_rc.set("Please input a valid canteen.")


#remove canteen
def remove_canteen_a(canteendata, canteen):
    del canteendata['canteen'][canteen]
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


#obtain booth to remove
def obtain_booth_to_remove(canteendata, canteen, booth):
    booth = booth.get()
    rb_f3 = Toplevel()
    msg_rb2 = StringVar()
    Label(rb_f3, textvariable = msg_rb2).pack()
    if check_booth(canteendata, canteen, booth):
        remove_booth_a(canteendata,canteen,booth)
        msg_rb2.set("Done!")
    else:
        msg_rb2.set("Please input a valid booth.")


#remove booth
def remove_booth_a(canteendata, canteen, booth):
    del canteendata['canteen'][canteen]["booths"][booth]
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


#obtain food to remove
def obtain_food_to_remove(canteendata, canteen, booth, food):
    food = food.get()
    rf_f4 = Toplevel()
    msg_rf3 = StringVar()
    Label(rf_f4, textvariable = msg_rf3).pack()
    if check_food(canteendata, canteen, booth, food):
        remove_food_a(canteendata,canteen,booth, food)
        msg_rf3.set("Done!")
    else:
        msg_rf3.set("Please input a valid food.")


#remove food
def remove_food_a(canteendata, canteen, booth, food):
    del canteendata['canteen'][canteen]["booths"][booth][food]
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)


################################################################
#Add or change canteen data function

def add_or_change_data(canteendata):
    ac_screen = Toplevel()
    Button(ac_screen, text="Add canteen", command = lambda:add_canteen(canteendata)).pack()
    Button(ac_screen, text="Add booth", command = lambda:add_booth(canteendata)).pack()
    Button(ac_screen, text="Add food", command = lambda:add_food(canteendata)).pack()
    Button(ac_screen, text="Change price", command = lambda:change_price(canteendata)).pack()
    Button(ac_screen, text="Add/change address", command = lambda:add_change_address(canteendata)).pack()
    Button(ac_screen, text="Add/change canteen rank", command = lambda:add_change_rank(canteendata)).pack()

def add_canteen(canteendata):
    ac_screen = Toplevel()
    Label(ac_screen, text = "Please input canteen:").grid(row=0)
    canteen = Entry(ac_screen)
    canteen.grid(row=0,column=1)
    Button(ac_screen, text="submit", command=lambda:obtain_canteen(canteendata, canteen)).grid(row=0,column=2)


def add_booth(canteendata):
    ab_screen = Toplevel()
    Label(ab_screen, text = "Please input canteen:").grid(row=0)
    canteen = Entry(ab_screen)
    canteen.grid(row=0,column=1)
    Button(ab_screen, text="submit", command=lambda:obtain_boothba(canteendata, canteen)).grid(row=0,column=2)

def obtain_boothba(canteendata, canteen):
    canteen = canteen.get()
    ab_f2 = Toplevel()
    msg_ab1 = StringVar()
    Label(ab_f2, textvariable = msg_ab1).grid(row=1)
    if check_canteen(canteendata, canteen):
        Label(ab_f2, text = "Please input booth:").grid(row=0)
        booth = Entry(ab_f2)
        booth.grid(row=0,column=1)
        Button(ab_f2, text="submit", command=lambda:obtain_booth(canteendata,canteen, booth)).grid(row=0,column=2)
    else:
        msg_ab1.set("Please input a valid canteen.")


###############################################################################################################################
#add food
def add_food(canteendata):
    af_screen = Toplevel()
    Label(af_screen, text = "Please input canteen:").grid(row=0)
    canteen = Entry(af_screen)
    canteen.grid(row=0,column=1)
    Button(af_screen, text="submit", command=lambda:obtain_foodba(canteendata,canteen)).grid(row=0,column=2)

def obtain_foodba(canteendata, canteen):
    canteen = canteen.get()
    af_f2 = Toplevel()
    msg_af1 = StringVar()
    Label(af_f2, textvariable = msg_af1).grid(row=1)
    if check_canteen(canteendata, canteen):
        if any(canteendata['canteen'][canteen]['booths'].items()):
            Label(af_f2, text = "Please input booth:").grid(row=0)
            booth = Entry(af_f2)
            booth.grid(row=0,column=1)
            Button(af_f2, text="submit", command=lambda:obtain_foodfa(canteendata,canteen, booth)).grid(row=0,column=2)
        else:
            msg_af1.set("This canteen does not have booth.")
    else:
        msg_af1.set("Please input a valid canteen.")

def obtain_foodfa(canteendata, canteen, booth):
    booth = booth.get()
    af_f3 = Toplevel()
    msg_af3 = StringVar()
    Label(af_f3, textvariable = msg_af3).grid(row=1)
    if check_booth(canteendata, canteen, booth):
        Label(af_f3, text = "Please input food:").grid(row=0)
        food = Entry(af_f3)
        food.grid(row=0,column=1)
        Button(af_f3, text="submit", command=lambda:obtain_food_and_price(canteendata,canteen,booth,food)).grid(row=0,column=2)
    else:
        msg_af3.set("Please input a valid booth.")

def obtain_food_and_price(canteendata, canteen, booth,food):
    food = food.get()
    af_f4 = Toplevel()
    msg_af4 = StringVar()
    Label(af_f4, textvariable = msg_af4).grid(row=1)
    if check_food(canteendata, canteen, booth, food):
        msg_af4.set("This food exist.")
    else:
        Label(af_f4, text = "Please input price:").grid(row=0)
        price = Entry(af_f4)
        price.grid(row=0,column=1)
        Button(af_f4, text="submit", command=lambda:obtain_food_and_price_a(canteendata,canteen,booth,food,price)).grid(row=0,column=2)


##########################################################################################################################################3
# change price

def change_price(canteendata):
    cp_screen = Toplevel()
    Label(cp_screen, text = "Please input canteen:").grid(row=0)
    canteen = Entry(cp_screen)
    canteen.grid(row=0,column=1)
    Button(cp_screen, text="submit", command=lambda:obtain_pricebc(canteendata,canteen)).grid(row=0,column=2)

def obtain_pricebc(canteendata, canteen):
    canteen = canteen.get()
    cp_f2 = Toplevel()
    msg_cp1 = StringVar()
    Label(cp_f2, textvariable = msg_cp1).grid(row=1)
    if check_canteen(canteendata, canteen):
        if any(canteendata['canteen'][canteen]['booths'].items()):
            Label(cp_f2, text = "Please input booth:").grid(row=0)
            booth = Entry(cp_f2)
            booth.grid(row=0,column=1)
            Button(cp_f2, text="submit", command=lambda:obtain_pricefc(canteendata,canteen, booth)).grid(row=0,column=2)
        else:
            msg_cp1.set("This canteen does not have booth.")
    else:
        msg_cp1.set("Please input a valid canteen.")

def obtain_pricefc(canteendata, canteen, booth):
    booth = booth.get()
    cp_f3 = Toplevel()
    msg_cp3 = StringVar()
    Label(cp_f3, textvariable = msg_cp3).grid(row=1)
    if check_booth(canteendata, canteen, booth):
        if any(canteendata['canteen'][canteen]['booths'][booth].items()):
            Label(cp_f3, text = "Please input food:").grid(row=0)
            food = Entry(cp_f3)
            food.grid(row=0,column=1)
            Button(cp_f3, text="submit", command=lambda:obtain_food_and_price_c(canteendata,canteen,booth,food)).grid(row=0,column=2)
        else:
            msg_cp3.set("This booth does not have food.")
    else:
        msg_cp3.set("Please input a valid booth.")

def obtain_food_and_price_c(canteendata, canteen, booth,food):
    food = food.get()
    cp_f4 = Toplevel()
    msg_cp4 = StringVar()
    Label(cp_f4, textvariable = msg_cp4).grid(row=1)
    if check_food(canteendata, canteen, booth, food):
        Label(cp_f4, text = "Please input price:").grid(row=0)
        price = Entry(cp_f4)
        price.grid(row=0,column=1)
        Button(cp_f4, text="submit", command=lambda:obtain_food_and_price_ca(canteendata,canteen,booth,food,price)).grid(row=0,column=2)
    else:
        msg_cp4.set("This food does not exist.")
####################################################################################################################################################
            
def add_change_address(canteendata):
    aa_screen = Toplevel()
    Label(aa_screen, text = "Please input canteen:").grid(row=0)
    canteen = Entry(aa_screen)
    canteen.grid(row=0,column=1)
    Button(aa_screen, text="submit", command=lambda:obtain_address(canteendata,canteen)).grid(row=0,column=2)

def obtain_address(canteendata, canteen):
    canteen = canteen.get()
    aa_f2 = Toplevel()
    msg_aa1 = StringVar()
    Label(aa_f2, textvariable = msg_aa1).grid(row=1)
    if check_canteen(canteendata, canteen):
            Label(aa_f2, text = "Please input address:").grid(row=0)
            address = Entry(aa_f2)
            address.grid(row=0,column=1)
            Button(aa_f2, text="submit", command=lambda:obtain_address_a(canteendata,canteen, address)).grid(row=0,column=2)
    else:
        msg_aa1.set("Please input a valid canteen.")

#####################################################################################################################################################
def add_change_rank(canteendata):
    ar_screen = Toplevel()
    Label(ar_screen, text = "Please input canteen:").grid(row=0)
    canteen = Entry(ar_screen)
    canteen.grid(row=0,column=1)
    Button(ar_screen, text="submit", command=lambda:obtain_rank(canteendata,canteen)).grid(row=0,column=2)

def obtain_rank(canteendata, canteen):
    canteen = canteen.get()
    ar_f2 = Toplevel()
    msg_ar1 = StringVar()
    Label(ar_f2, textvariable = msg_ar1).grid(row=1)
    if check_canteen(canteendata, canteen):
            Label(ar_f2, text = "Please input rank:").grid(row=0)
            rank = Entry(ar_f2)
            rank.grid(row=0,column=1)
            Button(ar_f2, text="submit", command=lambda:obtain_address_a(canteendata,canteen, rank)).grid(row=0,column=2)
    else:
        msg_ar1.set("Please input a valid canteen.")



            
#############################################################################################################
#Remove data function
def remove_data(canteendata):
    r_screen = Toplevel()
    Button(r_screen, text="Remove canteen", command = lambda:remove_canteen()).pack()
    Button(r_screen, text="Remove booth", command = lambda:remove_booth()).pack()
    Button(r_screen, text="Remove food", command = lambda:remove_food()).pack()


def remove_canteen():
    rc_screen = Toplevel()
    Label(rc_screen, text = "Please input canteen:").grid(row=0)
    canteen = Entry(rc_screen)
    canteen.grid(row=0,column=1)
    Button(rc_screen, text="submit", command=lambda:obtain_canteen_to_remove(canteendata, canteen)).grid(row=0,column=2)


def remove_booth():
    rb_screen = Toplevel()
    Label(rb_screen, text = "Please input canteen:").grid(row=0)
    canteen = Entry(rb_screen)
    canteen.grid(row=0,column=1)
    Button(rb_screen, text="submit", command=lambda:obtain_boothb(canteendata,canteen)).grid(row=0,column=2)

def obtain_boothb(canteendata, canteen):
    canteen = canteen.get()
    rb_f2 = Toplevel()
    msg_rb1 = StringVar()
    Label(rb_f2, textvariable = msg_rb1).grid(row=1)
    if check_canteen(canteendata, canteen):
        if any(canteendata['canteen'][canteen]['booths'].values()):
            Label(rb_f2, text = "Please input booth:").grid(row=0)
            booth = Entry(rb_f2)
            booth.grid(row=0,column=1)
            Button(rb_f2, text="submit", command=lambda:obtain_booth_to_remove(canteendata,canteen,booth)).grid(row=0,column=2)
        else:
            msg_rb1.set("This canteen does not have booth.")
    else:
        msg_rb1.set("Please input a valid canteen.")


def remove_food():
    rf_screen = Toplevel()
    Label(rf_screen, text = "Please input canteen:").grid(row=0)
    canteen = Entry(rf_screen)
    canteen.grid(row=0,column=1)
    Button(rf_screen, text="submit", command=lambda:obtain_foodb(canteendata,canteen)).grid(row=0,column=2)

def obtain_foodb(canteendata, canteen):
    canteen = canteen.get()
    rf_f2 = Toplevel()
    msg_rf1 = StringVar()
    Label(rf_f2, textvariable = msg_rf1).grid(row=1)
    if check_canteen(canteendata, canteen):
        if any(canteendata['canteen'][canteen]['booths'].values()):
            Label(rf_f2, text = "Please input booth:").grid(row=0)
            booth = Entry(rf_f2)
            booth.grid(row=0,column=1)
            Button(rf_f2, text="submit", command=lambda:obtain_foodf(canteendata,canteen, booth)).grid(row=0,column=2)
        else:
            msg_rf1.set("This canteen does not have booth.")
    else:
        msg_rf1.set("Please input a valid canteen.")

def obtain_foodf(canteendata, canteen, booth):
    booth = booth.get()
    rf_f3 = Toplevel()
    msg_rf3 = StringVar()
    Label(rf_f3, textvariable = msg_rf3).grid(row=1)
    if check_booth(canteendata, canteen, booth):
        if any(canteendata['canteen'][canteen]['booths'][booth].values()):
            Label(rf_f3, text = "Please input food:").grid(row=0)
            food = Entry(rf_f3)
            food.grid(row=0,column=1)
            Button(rf_f3, text="submit", command=lambda:obtain_food_to_remove(canteendata,canteen,booth,food)).grid(row=0,column=2)
        else:
            msg_rf3.set("This booth does not have food.")
    else:
        msg_rf3.set("Please input a valid booth.")

            



##############################################################################################################
#Functions for update data

def update(canteendata):
    f_screen = Toplevel()
    Button(f_screen, text="Add/change data", command = lambda:add_or_change_data(canteendata)).pack()
    Button(f_screen, text="Remove data", command = lambda:remove_data(canteendata)).pack()

#############################################################################################################
#Opens json file 
with open('canteen.json', 'r') as f:
    canteendata = json.load(f)

root = Tk()
Button(root, text="Configure", command = lambda:update(canteendata)).pack()

root.mainloop()


        









