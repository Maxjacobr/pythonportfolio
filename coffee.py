#Max Rubenstein
#Coffee shop

def coffee():
    print("Welcome to Shmeep Coffee Shop!")

    temp = input("Do you want a hot or cold drink? ")
#This is hot route
    if temp == "hot":
        sweet = input("Sounds good, and would you like your drink to be sweet or bitter? ")
        if sweet == "bitter":
            print("Here is your black coffee. Enjoy!")
        elif sweet == "sweet":
            print("Here is your hot chocolate. Enjoy!")
        else:
            print("Please send your answer without capital letters and try again")
#This is cold route
    elif temp == "cold":
        sweet = input("Sounds good, and would you like your drink to be sweet or bitter? ")
        if sweet == "bitter":
            print("Here is your cold brew. Enjoy!")
        elif sweet == "sweet":
            print("Here is your iced latte. Enjoy!")
        else:
            print("Please send your answer without capital letters and try again")
    else:
        print("Please send your answer without capital letters and try again")
coffee()
