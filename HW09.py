"""
Georgia Institute of Technology - CS1301
HW09 -  Recursion
"""
#########################################
"""
Function Name: hoursWorked()
Parameters: clockedHours (list)
Returns:  totalHours (int)
"""
def hoursWorked(clockedHours):
    if len(clockedHours)==0:
        return 0
    else:
        return clockedHours[0]+hoursWorked(clockedHours[1:])
#########################################
"""
Function Name: secretLocation()
Parameters: location (str)
Returns: decodedLocation (str)
"""
def secretLocation(location):
    if len(location) == 0:
        return ""
    else:
        if location[0] in "abcdefghijklmnopqrstuvwxyz" or location[0] == " ":
            return location[0] + secretLocation(location[1:])
        else:
            return secretLocation(location[1:])
#########################################
"""
Function Name: springRegistration()
Parameters: originalCRNs (list)
Returns: finalCRNs (list)
"""
def springRegistration(originalCRNs):
    if len(originalCRNs) == 0:
        return []
    else:
        r = springRegistration(originalCRNs[1:])
        if originalCRNs[0] not in r:
            r = [originalCRNs[0]]+r
        return r
#########################################
"""
Function Name: poncePlanner()
Parameters: restaurantChoices (list)
Returns: taFavorites (dict)
"""
def poncePlanner(restaurantChoices):
    if len(restaurantChoices) == 0:
        return {}
    else:
        taFavorites = poncePlanner(restaurantChoices[1:])
        taFavorites[restaurantChoices[0][0]] = restaurantChoices[0][1]
        return taFavorites
    

#########################################
"""
Function Name: drawRectangle()
Parameters: width (int), height (int)
Returns:  None (NoneType)
"""
def drawRectangle(width, height):
    if width < 3:
        print("You're cutting corners!")
    else:
        if height == 1:
            print("*"*width)
        elif height == width:
            print("*"*width)
            drawRectangle(width,height-1)
        else:
            print("*" + " "*(width-2) + "*")
            drawRectangle(width,height-1)
            
            

