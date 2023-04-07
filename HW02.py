"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: availableDate()
Parameters: date(int), isWeekend(bool)
Returns: availability(str)
"""
def availableDate(date, isWeekend):
    if date%2 == 0 or isWeekend == True:
        return('Available on %d!' % (date))
    else:
        return('Not available :(')
    

#########################################

"""
Function Name: buyGame()
Parameters: gameTitle(str), budget(float), cost(float), positiveRating(float)
Returns: None(NoneType)
"""
def buyGame(gameTitle, budget, cost, positiveRating):   
    if cost <= budget and positiveRating >= .7:
        print('Sasuke will buy %s!' % (gameTitle))
    elif cost <= budget and positiveRating < .7:
        print("Let's find another game.")
    else:
        print(gameTitle + " is over $" + str(budget) + "!")
    

#########################################

"""
Function Name: foodTime()
Parameters: restaurant(str), time(int)
Returns: howLong(float or int)
"""
def foodTime(restaurant, time):
    if restaurant == "Cafe Leblanc":
        howLong = float(time-15-(2*(620/80)))
    elif restaurant == "The Roost":
        howLong = float(time-20-(2*(700/80)))
    elif restaurant == "Lumpy Pumpkin":
        howLong = float(time-22-(2*(850/80)))
    elif restaurant == "The Milk Bar":
        howLong = float(time-13-(2*(1200/80)))
    else:
        howLong = "Please use a different input"
        
    if howLong < 0:
            howLong = -1
    return(howLong)

#########################################

"""
Function Name: restaurantReservation()
Parameters: total(int), toSave(int), average(int)
Returns: canReserve(bool)
"""
def restaurantReservation(total, toSave, average):
    leftover = total-toSave-(2*average)
    if leftover >= 0:
        canReserve = True
    else:
        canReserve = False
    return(canReserve)

#########################################

"""
Function Name: halloweenHeist()
Parameters: num1(int), num2(int), name(str)
Returns: message(str)
"""
def halloweenHeist(num1, num2, name):
    num = num1-num2
    if num > 0:
        return('%s has the package.' % (name))
    elif num < 0:
        return('%s does not have the package.' % (name))
    else:
        return('%s has taken over.' % (name))
    
