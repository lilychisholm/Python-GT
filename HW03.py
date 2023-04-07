"""
Georgia Institute of Technology - CS1301
HW03 -  Loops and Iteration
"""
#########################################
"""
Function Name: product()
Parameters: nums(str)
Returns: product(int)
"""
def product(nums):
    product = 1
    for number in nums:
        product *= int(number)
    return product
    print(product)

def recipeCount(recipe):
    totalTeaspoons = 0
    for thing in recipe:
        if thing.isdigit():
            totalTeaspoons += int(thing)
    return totalTeaspoons
    print(totalTeaspoons)

def instagraminator(usernames):
    decodedUsernames = ""
    for character in usernames:
        if character != "@" and character != "_" and character != "$":
            decodedUsernames+=character
    print(decodedUsernames)
    return decodedUsernames

def studentLoans(loanAmount):
    forgivenessCount = 0
    while loanAmount > 0:
        loanAmount -= 10000
        forgivenessCount+= 1
    return forgivenessCount
    print(forgivenessCount)
        
def playoffs(team1name, team2name, scoreCount):
    team1score = 0
    team2score = 0
    for score in scoreCount:
        if score == "1":
            team1score += 1
        elif score == "2":
            team2score += 1
    if team1score > team2score:
        return team1name + " has won the game!"
    elif team2score > team1score:
        return team2name + " has won the game!"
    else:
        return "It was a tie :("
    
