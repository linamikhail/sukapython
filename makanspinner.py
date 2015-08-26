# MAKAN SPINNER: Help You to Choose What to Have for Breakfast Today
# Python Codes Example for Randomizing Items
# No Copyright Necessary
# Trademark Belongs to the Originator
# Version 1.0
# Date 26.AUGUST.2015

from random import randint
FOOD = ["Nasi Lemak", "Mee Hoon", "Roti Canai", "Roti Bakar Kaya", "Kuew Tiau", "Mee Goreng Mamak"]
DRINKS = ["Teh O", "Kopi O", "Teh Tarik", "Milo", "Air Kosong", "Kopi Susu", "Horlicks"]
LOCATION = ["Restoran Mamak", "Masak Sendiri", "Bungkus", "Gerai Tepi Jalan", "Foodcourt"]

print("###MAKAN SPINNER: Breakfast Random Selector.###")
userinput = input("Press ENTER to start spinning or 'Q' to Quit: ")

def twistdice():
    """
    Function to randomize items in the list given above.
    """
    chooseFood = randint(0,3)
    chooseDrinks = randint(0,3)
    chooseLocation = randint(0,3)
    print ("FOOD: ")
    print (FOOD[chooseFood])
    print ("DRINKS: ")
    print (DRINKS[chooseDrinks])
    print ("LOCATION: ")
    print (LOCATION[chooseLocation])

while userinput != "Q":
    print(twistdice())
    userinput = input("Press ENTER to start spinning or 'Q' to Quit: ")
    if userinput == "q":
        userinput2 = input("Do you mean 'Q' (Y/N)?")
        if userinput2 == "Y" or userinput2 == "y":
                quit();
