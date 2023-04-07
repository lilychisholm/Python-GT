"""
Georgia Institute of Technology - CS1301
HW06 -  Dictionaries and Try/Except
"""
#########################################
"""
Function Name: dinnerTimer()
Parameters: meal (str), diningHalls (dict)
Returns: optionsList (list)
"""
def dinnerTime(meal, diningHalls):
    optionsList = []
    for hall in diningHalls:
        for meals in diningHalls[hall]:
            if meals.lower == meal.lower and hall not in optionsList:
                optionsList.append(hall)
    if optionsList == []:
        optionsList = "Eat at home!"
    return optionsList
                

#########################################
"""
Function Name: rateActor()
Parameters: skillScore (list), fanScore (List)
Returns: totalScores (dict)
"""
def rateActor(skillScore, fanScore):
    totalScores = {}
    for set in range(len(skillScore)):
        try:
            skillScore[set][1] + fanScore[set][1]
        except:
            if ((type(skillScore[set][1]) != int and type(skillScore[set][1]) != float) or (type(skillScore[set][1]) == None)) and ((type(fanScore[set][1]) != int and type(fanScore[set][1]) != float)  or (type(fanScore[set][1]) == None)):
                totalScores[skillScore[set][0]] = 0
            if (type(skillScore[set][1]) != int and type(skillScore[set][1]) != float) or (type(skillScore[set][1]) == None):
                skillScore[set] = (skillScore[set][0], 0)
                totalScores[skillScore[set][0]] = int(float(fanScore[set][1]) + float(skillScore[set][1])+3)
            if (type(fanScore[set][1]) != int and type(fanScore[set][1]) != float)  or (type(fanScore[set][1]) == None):
                fanScore[set] = (fanScore[set][0], 0)
                totalScores[skillScore[set][0]] = int(float(fanScore[set][1]) + float(skillScore[set][1])+3)
        else:
            totalScores[skillScore[set][0]] = int(float(fanScore[set][1]) + float(skillScore[set][1]))
    
    return totalScores

#########################################
"""
Function Name: theRealDeal()
Parameters: stockDict (dict), goodStock (str)
Returns: richList (list)
"""
def theRealDeal(stockDict, goodStock):
    richList = []
    if goodStock not in stockDict:
        goods = 0
        richList = ["You haven't invested in this one yet!"]
        for stock in stockDict:
            goods = stockDict[stock][0] * stockDict[stock][1] * stockDict[stock][2]
            if goods > 7000:
                richList.append(stock)
    else:
        goody = 0
        for stock in stockDict:
            goody = stockDict[stock][0] * stockDict[stock][1] * stockDict[stock][2]
            if goody > 7000:
                richList.append(stock)
        richList.sort()
        richList.insert(0, stockDict[goodStock][0] * stockDict[goodStock][1] * stockDict[goodStock][2])     
    return richList

#########################################
"""
Function Name: flightsInfo()
Parameters: flightsDict(dict)
Returns: fixedflightsDict(dict)
"""
def flightsInfo(flightsDict):
    fixedflightsDict = {}
    listy = []
    for flight in flightsDict:
        for number in range(len(flightsDict[flight]["passengers"])):
            if len(flightsDict[flight]["passengers"][number]) != 3:
                if len(flightsDict[flight]["passengers"][number][0]) <= 5:
                    listy.append((flightsDict[flight]["passengers"][number][0],
                    flightsDict[flight]["passengers"][number][1], "A"))
                elif len(flightsDict[flight]["passengers"][number][0]) == 6:
                    listy.append((flightsDict[flight]["passengers"][number][0],
                    flightsDict[flight]["passengers"][number][1], "B"))
                else:
                    listy.append((flightsDict[flight]["passengers"][number][0],
                    flightsDict[flight]["passengers"][number][1], "Premium"))
            else:
                listy.append((flightsDict[flight]["passengers"][number]))
        flightsDict[flight]["passengers"] = listy
        listy = []
        fixedflightsDict = flightsDict
    return fixedflightsDict

#########################################
"""
Function Name: fastFood()
Parameters: friendDict (dict), menu (dict)
Returns: friendsOwed (list)
"""
def fastFood(friendDict, menu):
    friendsOwed = []
    for friend in friendDict:
        total = 0
        for food in friendDict[friend]:
            total+=menu[food]
        friendsOwed.append((friend, total))
    friendsOwed.sort()           
    return friendsOwed
