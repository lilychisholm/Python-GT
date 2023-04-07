import math
"""
Georgia Institute of Technology - CS1301
HW01 - Functions & Expressions
"""

#########################################

"""
Function Name: tasteOfTech()
Parameters: N/A
Returns: None
"""
def tasteOfTech():
    name = input("What is your first name? ")
    tin_drum = float(input("How much did you spend at Tin Drum? "))
    waffle = float(input("How much did you spend at Waffle House? "))
    buffalo = float(input("How much did you spend at Buffalo Wild Wings? "))
    total = round((tin_drum + waffle + buffalo), 2)
    doge = round((tin_drum+waffle+buffalo)*14.57, 2)
    print("Congratulations " + name + "! You spent $" + str(total) + " in total and earned " + str(doge) + " DOGE.")
    

#########################################

"""
Function Name: shoppingMoney()
Parameters: N/A
Returns: None
"""
def shoppingMoney():
    income = int(input("How much is your monthly income? "))
    leftover = income - 700 - (80*4)
    savings = (leftover)*.6
    spending = float(leftover)-float(savings)
    print("You can save $" + str(round(savings, 2)) + " and spend the remaining $" + str(round(spending, 2)) + " on anything this month.")
    
#########################################

"""
Function Name: houseParty()
Parameters: N/A
Returns: None
"""
def houseParty():
    nuggets_per_person = int(input("How many chicken nuggets will each guest eat? "))
    onionrings_per = int(input("How many onion rings will each guest eat? "))
    donuts_per = int(input("How many donuts will each guest eat? "))
    cookies_per = int(input("How many cookies will each guest eat? "))
    guests = int(input("How many guests are you expecting at the party? "))
    nuggs = str(nuggets_per_person * guests)
    rings = str(onionrings_per * guests)
    donuts = str(donuts_per * guests)
    cookies = str(cookies_per * guests)
    print("You need to buy " + nuggs + " chicken nuggets, " + rings + " onion rings, " + donuts + " donuts and " + cookies + " cookies for " + str(guests) + " guests.")
                             

#########################################

"""
Function Name: spareTime()
Parameters: N/A
Returns: None
"""
def spareTime():
    weeklyhours = 112
    credithours = int(input("How many credits are you taking? "))
    study = credithours * 3
    spare = weeklyhours - credithours - study
    daily = spare/7
    rounded = math.floor(daily)
    minutes = round(((daily-rounded)*60), 1)
    print("You have " + str(rounded) + " hours and " + str(minutes) + " minutes per day to spare for other activities.")
    
    
                      
    

#########################################

"""
Function Name: ratsNight()
Parameters: N/A
Returns: None
"""
def ratsNight():
    gameSlots = int(input("How many slots would you like to book for video games? "))
    triviaSlots = int(input("How many slots woould you like to book for trivia time? "))
    artsCraftsSlots = int(input("How many slots would you like to book for arts/crafts? "))
    time = (gameSlots * 30) + (triviaSlots * 10) + (artsCraftsSlots * 45)
    rounded = math.floor(time/60)*60
    leftovermin = time-rounded
    print("You will spend " + str(int(rounded/60)) + " hours and " + str(int(leftovermin)) + " minutes at Rats Night.")
                    
