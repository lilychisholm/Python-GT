import math
"""
Georgia Institute of Technology - CS1301
HW11
"""
#########################################
"""
Function Name: santaHelper()
Parameters: kids (list)
Returns:  destinations (dict)
"""
def santaHelper(kids):
    if kids == []:
        return {}
    else:
        niceys = santaHelper(kids[:-1])
        name,isNice,location = kids[-1]
        if isNice == True:
            if location not in niceys:
                niceys[location] = [name]
            else:
                niceys[location].append(name)
                niceys[location].sort()
    return niceys
#########################################
"""
Function Name: myWishlist()
Parameters: stores (dict)
Returns: None (NoneType)
"""
def myWishList(stores):
    wishlist = open("wishlist.txt","w")
    wishlist.write("My WishList")
    newdict = {}
    for store in stores:
        for item in stores[store]:
            if item[0] not in newdict:
                newdict[item[0]] = [(item[1], store)]
                newdict[item[0]].sort()
            else:
                newdict[item[0]].append((item[1], store))
                newdict[item[0]].sort()
    for thing in newdict:
        wishlist.write("\n\n{}:\n".format(thing))
        for storey in newdict[thing]:
            wishlist.write("\n{}".format(storey[1]))
    wishlist.close()
#########################################
"""
Function Name: getMessage()
Parameters: presaleCode (int)
Returns: message (str)
"""
def getMessage(presaleCode):
    message = ""
    while presaleCode != 0:
        thing = presaleCode%16
        if thing >= 10:
            if thing == 10:
                thing = "A"
            elif thing == 11:
                thing = "B"
            elif thing == 12:
                thing = "C"
            elif thing == 13:
                thing = "D"
            elif thing == 14:
                thing = "E"
            elif thing == 15:
                thing = "F"
        message+=str(thing)
        presaleCode = math.floor(presaleCode/16)
    message = message[::-1]
    return message
#########################################
"""
Function Name: buildFrosty()
Parameters: materials (dict)
Returns: snowManStr (str)
"""
def buildFrosty(materials):
    sticks = 0
    rocks = 0
    carrots = 0
    hats = 0
    for person in materials:
        if "sticks" in materials[person]:
            sticks += materials[person]["sticks"]
        if "rocks" in materials[person]:
            rocks += materials[person]["rocks"]
        if "carrot" in materials[person]:
            carrots+= materials[person]["carrot"]
        if "hat" in materials[person]:
            hats += materials[person]["hat"]
    if hats >= 1 and sticks >= 2 and rocks >= 10 and carrots >= 1:
        snowManStr = "We have enough materials to build the snowman :)"
    else:
        snowManStr = "Not enough materials :("
    return snowManStr

#########################################
"""
Function Name: guideBuddy()
Parameters: locationDict(dict), movementsList(list)
Returns:  newRoutine (str)
"""
def distance(alist, blist):
    return math.sqrt((alist[0] - blist[0])**2 + (alist[1] - blist[1])**2)
def guideBuddy(locationDict,movementsList):
    x = 0
    y = 0
    for item in movementsList:
        if item == "right":
            y += 1
        elif item == "left":
            y-=1
        elif item == "up":
            x+=1
        else:
            x-=1
            
    coord = [x,y]
    closest = ""
    numby = 10*100
    for place in locationDict:
        if distance(coord,locationDict[place]) < numby:
            closest = place
            numby = distance(coord,locationDict[place])
    return "Go to {}!".format(closest)
        


## helper method for guideBuddy
## alist and blist are lists of length 2 containing locations

