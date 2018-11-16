import json
from tkinter import *

with open('canteen.json', 'r') as f:
    canteendata = json.load(f)
#Split into 2 major parts
# 1) Add or Change data
# 2) Remove data
###################################################################################################################################################
#functions to check if data exists


#check if canteen exists
def check_canteen(canteendata, canteen):
    exist = False
    for existing_canteen in canteendata['canteen']:
        if canteen == existing_canteen:
            exist = True
    return exist
        

#check if booth exist
def check_booth(canteendata, canteen, booth):
    exist = False
    for existing_booths in canteendata['canteen'][canteen]['booths']: 
        if booth == existing_booths:
            exist = True
            break
    return exist


#check if food exists
def check_food(canteendata, canteen, booth, food):
    exist = False
    for existing_food in canteendata['canteen'][canteen]['booths'][booth]: 
        if existing_food == food:
            exist = True
            break
    return exist



#################################################################################################################
#Add or change canteen data function

def add_or_change_data(canteendata):
    ac_screen = Toplevel()
    Button(ac_screen, text="Add canteen", command = lambda:add_canteen(canteendata)).pack()
    Button(ac_screen, text="Add booth", command = lambda:add_booth(canteendata)).pack()
    Button(ac_screen, text="Add food", command = lambda:add_food(canteendata)).pack()
    Button(ac_screen, text="Change price", command = lambda:change_price(canteendata)).pack()
    Button(ac_screen, text="Add/change address", command = lambda:add_change_address(canteendata)).pack()
    Button(ac_screen, text="Add/change canteen rank", command = lambda:add_change_rank(canteendata)).pack()

####################################################################################################################
#Adding canteen

def add_canteen(canteendata):
    ac_screen = Toplevel()
    Label(ac_screen, text = "Please input canteen to add:").grid(row=0)
    canteen = Entry(ac_screen)
    canteen.grid(row=0,column=1)
    Button(ac_screen, text="submit", command=lambda:obtain_canteen_ac(canteendata, canteen,ac_screen)).grid(row=0,column=2)


def obtain_canteen_ac(canteendata, canteen, ac_screen):
    canteen = canteen.get()
    ac_screen.destroy()
    ac_f2 = Toplevel()
    msg_ac = StringVar()
    Label(ac_f2, textvariable = msg_ac).pack()
    if check_canteen(canteendata, canteen):
        msg_ac.set("This canteen exists.")
    else:
        msg_ac.set("Done!")
        add_canteen_ac(canteendata, canteen)


def add_canteen_ac (canteendata, canteen):
    canteendata['canteen'][canteen] = {}
    canteendata['canteen'][canteen]["address"] = None
    canteendata['canteen'][canteen]["booths"] = {}
    canteendata['canteen'][canteen]["rank"] = None
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)
#################################################################################################################
#add booth
def add_booth(canteendata):
    ab_screen = Toplevel()
    Label(ab_screen, text = "Please input canteen with booth:").grid(row=0)
    canteen = Entry(ab_screen)
    canteen.grid(row=0,column=1)
    Button(ab_screen, text="submit", command=lambda:obtain_canteen_ab(canteendata, canteen,ab_screen)).grid(row=0,column=2)

def obtain_canteen_ab(canteendata, canteen, ab_screen):
    canteen = canteen.get()
    ab_screen.destroy()
    ab_f2 = Toplevel()
    msg_ab1 = StringVar()
    Label(ab_f2, textvariable = msg_ab1).grid(row=1)
    if check_canteen(canteendata, canteen):
        Label(ab_f2, text = "Please input booth to add:").grid(row=0)
        booth = Entry(ab_f2)
        booth.grid(row=0,column=1)
        Button(ab_f2, text="submit", command=lambda:obtain_booth_ab(canteendata,canteen, booth,ab_f2)).grid(row=0,column=2)
    else:
        msg_ab1.set("Please input a valid canteen.")

#retrieve and check booth
def obtain_booth_ab(canteendata, canteen, booth,ab_f2):
    booth = booth.get()
    ab_f2.destroy()
    ab_f3 = Toplevel()
    msg_ab2 = StringVar()
    Label(ab_f3, textvariable = msg_ab2).pack()
    if check_booth(canteendata, canteen, booth):
        msg_ab2.set("This booth exists.")
    else:
        msg_ab2.set("Done!")
        add_booth_ab(canteendata, canteen, booth)

#Adding booth to json
def add_booth_ab (canteendata, canteen, booth):
    canteendata['canteen'][canteen]["booths"][booth] = {}
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)
###############################################################################################################################
#add food
def add_food(canteendata):
    af_screen = Toplevel()
    Label(af_screen, text = "Please input canteen with food:").grid(row=0)
    canteen = Entry(af_screen)
    canteen.grid(row=0,column=1)
    Button(af_screen, text="submit", command=lambda:obtain_canteen_af(canteendata,canteen,af_screen)).grid(row=0,column=2)


def obtain_canteen_af(canteendata, canteen, af_screen):
    canteen = canteen.get()
    af_screen.destroy()
    af_f2 = Toplevel()
    msg_af1 = StringVar()
    Label(af_f2, textvariable = msg_af1).grid(row=1)
    if check_canteen(canteendata, canteen):
        if any(canteendata['canteen'][canteen]['booths'].items()):
            Label(af_f2, text = "Please input booth with food:").grid(row=0)
            booth = Entry(af_f2)
            booth.grid(row=0,column=1)
            Button(af_f2, text="submit", command=lambda:obtain_booth_af(canteendata,canteen, booth,af_f2)).grid(row=0,column=2)
        else:
            msg_af1.set("This canteen does not have booth.")
    else:
        msg_af1.set("Please input a valid canteen.")

def obtain_booth_af(canteendata, canteen, booth, af_f2):
    booth = booth.get()
    af_f2.destroy()
    af_f3 = Toplevel()
    msg_af3 = StringVar()
    Label(af_f3, textvariable = msg_af3).grid(row=1)
    if check_booth(canteendata, canteen, booth):
        Label(af_f3, text = "Please input food to add:").grid(row=0)
        food = Entry(af_f3)
        food.grid(row=0,column=1)
        Button(af_f3, text="submit", command=lambda:obtain_food_af(canteendata,canteen,booth,food,af_f3)).grid(row=0,column=2)
    else:
        msg_af3.set("Please input a valid booth.")

def obtain_food_af(canteendata, canteen, booth,food,af_f3):
    food = food.get()
    af_f3.destroy()
    af_f4 = Toplevel()
    msg_af4 = StringVar()
    Label(af_f4, textvariable = msg_af4).grid(row=1)
    if check_food(canteendata, canteen, booth, food):
        msg_af4.set("This food exist.")
    else:
        Label(af_f4, text = "Please input price:").grid(row=0)
        price = Entry(af_f4)
        price.grid(row=0,column=1)
        Button(af_f4, text="submit", command=lambda:obtain_price_af(canteendata,canteen,booth,food,price,af_f4)).grid(row=0,column=2)


def obtain_price_af(canteendata, canteen, booth, food, price, af_f4):
    price = price.get()
    af_f4.destroy()
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
        add_food_af(canteendata, canteen, booth, food, price)


#Adding food and price
def add_food_af (canteendata, canteen, booth, food, price):
    canteendata['canteen'][canteen]["booths"][booth][food] = price
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)
##########################################################################################################################################3
# change price

def change_price(canteendata):
    cp_screen = Toplevel()
    Label(cp_screen, text = "Please input canteen with food:").grid(row=0)
    canteen = Entry(cp_screen)
    canteen.grid(row=0,column=1)
    Button(cp_screen, text="submit", command=lambda:obtain_canteen_pc(canteendata,canteen,cp_screen)).grid(row=0,column=2)

def obtain_canteen_pc(canteendata, canteen, cp_screen):
    canteen = canteen.get()
    cp_screen.destroy()
    cp_f2 = Toplevel()
    msg_cp1 = StringVar()
    Label(cp_f2, textvariable = msg_cp1).grid(row=1)
    if check_canteen(canteendata, canteen):
        if any(canteendata['canteen'][canteen]['booths'].items()):
            Label(cp_f2, text = "Please input booth with food:").grid(row=0)
            booth = Entry(cp_f2)
            booth.grid(row=0,column=1)
            Button(cp_f2, text="submit", command=lambda:obtain_booth_pc(canteendata,canteen, booth, cp_f2)).grid(row=0,column=2)
        else:
            msg_cp1.set("This canteen does not have booth.")
    else:
        msg_cp1.set("Please input a valid canteen.")

def obtain_booth_pc(canteendata, canteen, booth, cp_f2):
    booth = booth.get()
    cp_f2.destroy()
    cp_f3 = Toplevel()
    msg_cp3 = StringVar()
    Label(cp_f3, textvariable = msg_cp3).grid(row=1)
    if check_booth(canteendata, canteen, booth):
        if any(canteendata['canteen'][canteen]['booths'][booth].items()):
            Label(cp_f3, text = "Please input food:").grid(row=0)
            food = Entry(cp_f3)
            food.grid(row=0,column=1)
            Button(cp_f3, text="submit", command=lambda:obtain_food_pc(canteendata,canteen,booth,food,cp_f3)).grid(row=0,column=2)
        else:
            msg_cp3.set("This booth does not have food.")
    else:
        msg_cp3.set("Please input a valid booth.")

def obtain_food_pc(canteendata, canteen, booth,food,cp_f3):
    food = food.get()
    cp_f3.destroy()
    cp_f4 = Toplevel()
    msg_cp4 = StringVar()
    Label(cp_f4, textvariable = msg_cp4).grid(row=1)
    if check_food(canteendata, canteen, booth, food):
        Label(cp_f4, text = "Please input new price:").grid(row=0)
        price = Entry(cp_f4)
        price.grid(row=0,column=1)
        Button(cp_f4, text="submit", command=lambda:obtain_price_pc(canteendata,canteen,booth,food,price,cp_f4)).grid(row=0,column=2)
    else:
        msg_cp4.set("This food does not exist.")


def obtain_price_pc(canteendata, canteen, booth, food, price,cp_f4):
    price = price.get()
    cp_f4.destroy()
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
        change_price_pc(canteendata, canteen, booth, food, price)


#Change price
def change_price_pc(canteendata, canteen, booth, food, price):
    canteendata['canteen'][canteen]["booths"][booth][food] = price
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)
####################################################################################################################################################
#update address


def add_change_address(canteendata):
    aa_screen = Toplevel()
    Label(aa_screen, text = "Please input canteen:").grid(row=0)
    canteen = Entry(aa_screen)
    canteen.grid(row=0,column=1)
    Button(aa_screen, text="submit", command=lambda:obtain_canteen_aa(canteendata,canteen,aa_screen)).grid(row=0,column=2)

def obtain_canteen_aa(canteendata, canteen,aa_screen):
    canteen = canteen.get()
    aa_screen.destroy()
    aa_f2 = Toplevel()
    msg_aa1 = StringVar()
    Label(aa_f2, textvariable = msg_aa1).grid(row=1)
    if check_canteen(canteendata, canteen):
            Label(aa_f2, text = "Please input address:").grid(row=0)
            address = Entry(aa_f2)
            address.grid(row=0,column=1)
            Button(aa_f2, text="submit", command=lambda:obtain_address_aa(canteendata,canteen, address,aa_f2)).grid(row=0,column=2)
    else:
        msg_aa1.set("Please input a valid canteen.")


def obtain_address_aa(canteendata, canteen, address,aa_f2):
    address = address.get()
    aa_f2.destroy()
    aa_f3 = Toplevel()
    Label(aa_f3, text= "Done").pack()
    change_address(canteendata, canteen, address)

def change_address (canteendata, canteen, address):
    canteendata['canteen'][canteen]["address"] = address
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)

#####################################################################################################################################################
#update rank
def add_change_rank(canteendata):
    ar_screen = Toplevel()
    Label(ar_screen, text = "Please input canteen:").grid(row=0)
    canteen = Entry(ar_screen)
    canteen.grid(row=0,column=1)
    Button(ar_screen, text="submit", command=lambda:obtain_rank(canteendata,canteen,ar_screen)).grid(row=0,column=2)

def obtain_rank(canteendata, canteen, ar_screen):
    canteen = canteen.get()
    ar_screen.destroy()
    ar_f2 = Toplevel()
    msg_ar1 = StringVar()
    Label(ar_f2, textvariable = msg_ar1).grid(row=1)
    if check_canteen(canteendata, canteen):
            Label(ar_f2, text = "Please input rank:").grid(row=0)
            rank = Entry(ar_f2)
            rank.grid(row=0,column=1)
            Button(ar_f2, text="submit", command=lambda:obtain_rank_ar(canteendata,canteen, rank,ar_f2)).grid(row=0,column=2)
    else:
        msg_ar1.set("Please input a valid canteen.")


def obtain_rank_ar(canteendata, canteen, rank,ar_f2):
    rank = rank.get()
    ar_f2.destroy()
    ar_f3 = Toplevel()
    Label(ar_f3, text= "Done").pack()
    change_rank(canteendata, canteen, rank)


def change_rank (canteendata, canteen, rank):
    canteendata['canteen'][canteen]["rank"] = rank
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)
            
#############################################################################################################
#Remove data function
#shows data to remove
def remove_data(canteendata):
    r_screen = Toplevel()
    Button(r_screen, text="Remove canteen", command = lambda:remove_canteen()).pack()
    Button(r_screen, text="Remove booth", command = lambda:remove_booth()).pack()
    Button(r_screen, text="Remove food", command = lambda:remove_food()).pack()


##################################################################################################################################
#remove canteen


def remove_canteen():
    rc_screen = Toplevel()
    Label(rc_screen, text = "Please input canteen to remove:").grid(row=0)
    canteen = Entry(rc_screen)
    canteen.grid(row=0,column=1)
    Button(rc_screen, text="submit", command=lambda:obtain_canteen_cr(canteendata, canteen,rc_screen)).grid(row=0,column=2)


#obtain canteen to remove
def obtain_canteen_cr(canteendata, canteen,rc_screen):
    canteen = canteen.get()
    rc_screen.destroy()
    rc_f2 = Toplevel()
    msg_rc = StringVar()
    Label(rc_f2, textvariable = msg_rc).pack()
    if check_canteen(canteendata, canteen):
        remove_canteen_data(canteendata,canteen)
        msg_rc.set("Done!")
    else:
        msg_rc.set("Please input a valid canteen.")


#remove canteen
def remove_canteen_data(canteendata, canteen):
    del canteendata['canteen'][canteen]
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)
##################################################################################################################################
# remove booth

def remove_booth():
    rb_screen = Toplevel()
    Label(rb_screen, text = "Please input canteen with booth:").grid(row=0)
    canteen = Entry(rb_screen)
    canteen.grid(row=0,column=1)
    Button(rb_screen, text="submit", command=lambda:obtain_canteen_br(canteendata,canteen,rb_screen)).grid(row=0,column=2)


def obtain_canteen_br(canteendata, canteen, rb_screen):
    canteen = canteen.get()
    rb_screen.destroy()
    rb_f2 = Toplevel()
    msg_rb1 = StringVar()
    Label(rb_f2, textvariable = msg_rb1).grid(row=1)
    if check_canteen(canteendata, canteen):
        if any(canteendata['canteen'][canteen]['booths'].items()):
            Label(rb_f2, text = "Please input booth to remove:").grid(row=0)
            booth = Entry(rb_f2)
            booth.grid(row=0,column=1)
            Button(rb_f2, text="submit", command=lambda:obtain_booth_br(canteendata,canteen,booth,rb_f2)).grid(row=0,column=2)
        else:
            msg_rb1.set("This canteen does not have booth.")
    else:
        msg_rb1.set("Please input a valid canteen.")


def obtain_booth_br(canteendata, canteen, booth,rb_f2):
    booth = booth.get()
    rb_f2.destroy()
    rb_f3 = Toplevel()
    msg_rb2 = StringVar()
    Label(rb_f3, textvariable = msg_rb2).pack()
    if check_booth(canteendata, canteen, booth):
        remove_booth_data(canteendata,canteen,booth)
        msg_rb2.set("Done!")
    else:
        msg_rb2.set("Please input a valid booth.")


#remove booth
def remove_booth_data(canteendata, canteen, booth):
    del canteendata['canteen'][canteen]["booths"][booth]
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)
###########################################################################################################################################
def remove_food():
    rf_screen = Toplevel()
    Label(rf_screen, text = "Please input canteen with food:").grid(row=0)
    canteen = Entry(rf_screen)
    canteen.grid(row=0,column=1)
    Button(rf_screen, text="submit", command=lambda:obtain_canteen_fr(canteendata,canteen,rf_screen)).grid(row=0,column=2)


def obtain_canteen_fr(canteendata, canteen,rf_screen):
    canteen = canteen.get()
    rf_screen.destroy()
    rf_f2 = Toplevel()
    msg_rf1 = StringVar()
    Label(rf_f2, textvariable = msg_rf1).grid(row=1)
    if check_canteen(canteendata, canteen):
        if any(canteendata['canteen'][canteen]['booths'].items()):
            Label(rf_f2, text = "Please input booth with food:").grid(row=0)
            booth = Entry(rf_f2)
            booth.grid(row=0,column=1)
            Button(rf_f2, text="submit", command=lambda:obtain_booth_fr(canteendata,canteen, booth,rf_f2)).grid(row=0,column=2)
        else:
            msg_rf1.set("This canteen does not have booth.")
    else:
        msg_rf1.set("Please input a valid canteen.")


def obtain_booth_fr(canteendata, canteen, booth,rf_f2):
    booth = booth.get()
    rf_f2.destroy()
    rf_f3 = Toplevel()
    msg_rf3 = StringVar()
    Label(rf_f3, textvariable = msg_rf3).grid(row=1)
    if check_booth(canteendata, canteen, booth):
        if any(canteendata['canteen'][canteen]['booths'][booth].items()):
            Label(rf_f3, text = "Please input food to remove:").grid(row=0)
            food = Entry(rf_f3)
            food.grid(row=0,column=1)
            Button(rf_f3, text="submit", command=lambda:obtain_food_fr(canteendata,canteen,booth,food,rf_f3)).grid(row=0,column=2)
        else:
            msg_rf3.set("This booth does not have food.")
    else:
        msg_rf3.set("Please input a valid booth.")

            

def obtain_food_fr(canteendata, canteen, booth, food,rf_f3):
    food = food.get()
    rf_f3.destroy()
    rf_f4 = Toplevel()
    msg_rf3 = StringVar()
    Label(rf_f4, textvariable = msg_rf3).pack()
    if check_food(canteendata, canteen, booth, food):
        remove_food_data(canteendata,canteen,booth, food)
        msg_rf3.set("Done!")
    else:
        msg_rf3.set("Please input a valid food.")


#remove food
def remove_food_data(canteendata, canteen, booth, food):
    del canteendata['canteen'][canteen]["booths"][booth][food]
    with open('canteen.json', 'w') as f:
        json.dump(canteendata,f, indent=2)

##############################################################################################################
#Update data home page

def update(canteendata):
    f_screen = Toplevel()
    Button(f_screen, text="Add/change data", command = lambda:add_or_change_data(canteendata)).pack()
    Button(f_screen, text="Remove data", command = lambda:remove_data(canteendata)).pack()

#############################################################################################################

root = Tk()
Button(root, text="Configure", command = lambda:update(canteendata)).pack()

root.mainloop()


        









