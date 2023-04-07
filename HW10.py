"""
Georgia Institute of Technology - CS1301
HW10 - OOP
"""
#########################################
class People:
  def __init__(self, name, age, isAsleep, canCook = False):
    self.name = name
    self.age = age
    self.isAsleep = isAsleep
    self.canCook = canCook
    self.friends = []
  def wakeUp(self):
    if self.isAsleep == True:
      self.isAsleep = False
    else:
      return ("{} is already awake.".format(self.name))
  def invite(self, friend):
    self.friends.append(friend)
  def __str__(self):
    if self.canCook == True:
      return ("My name is {} and I can cook.".format(self.name))
    else:
      return("My name is {} and I can't cook.".format(self.name))
  def __lt__(self, other):
    return (self.age < other.age)
    def __repr__(self): #provided
      return f"People({self.name}, {self.age}, {self.isAsleep}, {self.canCook}, {len(self.friends)})"

  def __eq__(self, other): #provided
    return self.name==other.name and self.age==other.age and self.isAsleep==other.isAsleep and self.canCook==other.canCook and self.friends==other.friends

#########################################
class Food:
  def __init__(self, name, ingredients, prepTime):
    self.name = name
    self.ingredients = ingredients
    self.prepTime = prepTime
  def __str__(self):
    return "{} takes {} to make.".format(self.name, self.prepTime)
  def __repr__(self): #provided
    return f"Food({self.name}, {len(self.ingredients)}, {self.prepTime})"

#########################################
class Activities:
  def __init__(self, ingredientsDict = {}):
    self.ingredientsDict = ingredientsDict

  def cook(self, food):
    dict2 = self.ingredientsDict.copy()
    for foody, numby in food.ingredients:
      dict2[foody] -= numby
      if dict2[foody] < 0:
        return "We did not have enough ingredients to make {}.".format(food.name)
    for foody, numby in food.ingredients:
      self.ingredientsDict[foody] -= numby
    return "We made {}!".format(food.name)
  def kidsTable(self, guests):
    guests.sort()
    list0 = guests[:4]
    listy = []
    for guest in list0:
      listy.append(guest.name)
    return listy
  def buyIngredients(self, ingredientName, ingredientAmount):
    if ingredientName in self.ingredientsDict:
      self.ingredientsDict[ingredientName] += ingredientAmount
    else:
      self.ingredientsDict[ingredientName] = ingredientAmount
      
  def __repr__(self): #provided
    return f"Activities({len(self.ingredientsDict)})"

  
