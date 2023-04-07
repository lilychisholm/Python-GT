"""
Georgia Institute of Technology - CS1301
HW03 -  Loops and Iteration
"""
#########################################
"""
Function Name: decodeString()
Parameters: encodedStr(str)
Returns: decodedList(list)
"""
def decodeString(encodedStr):
    decodedList = encodedStr[-1::-1]
    decodedList = decodedList.replace("@", "")
    decodedList = decodedList.lower()
    decodedList = list(decodedList.split("#"))
    return decodedList
    
#########################################
"""
Function Name: goodBrunch()
Parameters: ashList(list), nickList (list)
Returns: brunchDecision(list)
"""
def goodBrunch(ashList, nickList):
    brunchDecision = []
    brunchDecision1 = ""
    for item in ashList:
        for item2 in nickList:
            if item == item2:
                brunchDecision.append(item)
    if len(brunchDecision) > 1:
        brunchDecision = sorted(brunchDecision)
    if brunchDecision == []:
        brunchDecision = "Brunch at home it is!"
    if len(brunchDecision) == 1:
        for letter in brunchDecision:
            brunchDecision1 += letter
            brunchDecision = brunchDecision1

    return brunchDecision
    
    
#########################################
"""
Function Name: room_dist()
Parameters: dormMap (list), name1 (str), name2 (str)
Returns: distance (int)
"""
def room_dist(dormMap, name1, name2):
    position1 = []
    position2 = []
    for otherList in dormMap:
        for name in otherList:
            if name == name1:
                position1 = dormMap.index(otherList)
            elif name == name2:
                position2 = dormMap.index(otherList)
    distance = abs(position1 - position2)
    return distance
    
            
    
#########################################
"""
Function Name: freshProduce()
Parameters: veggies (list), prices (list)
Returns: veggieList (list)
"""
def freshProduce(veggies, prices):
    cost = 0
    veggieList = []
    for price in prices:
        if price < 4:
            cost += price
            veggieList.append(veggies[prices.index(price)])
    veggieList.append(cost)
    if len(veggieList) == 1:
        veggieList = []
    
    return veggieList
    

#########################################
"""
Function Name: find_roommate()
Parameters: my_interests(list), candidates (list), candidate_interests(list)
Returns: match (list)
"""
def find_roommate(my_interests, candidates, candidate_interests):
    matches = []
    interestcount = 0
    for listy in candidate_interests:
        for interest in listy:
            for minterest in my_interests:
                if interestcount >= 2:
                    interestcount = 0
                    matches.append(candidates[candidate_interests.index(listy)])
                if minterest == interest:
                    interestcount+=1
    if len(matches) > 1:
        del matches[-1]
    return matches

                        
                    
                        
    
    
    
    
