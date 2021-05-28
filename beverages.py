from ingredient import Ingredient
from item import Item
class Beverage:

    def __init__(self,name,ingredients):
        self.__name = name
        self.__ingredients = ingredients
    
    def checkIfEnoughIngredients(self, items):
        isEnough = True
        for ingredient in self.__ingredients:
            count = 0
            for item in items:
                if item.getName() != ingredient.getName():
                    count += 1
            if count == len(items):
                print(f"{self.__name} cannot be prepared because {ingredient.getName()} is not available")
                return False
        for ingredient in self.__ingredients:
                
            lackingIngredient = ingredient.getName()
            for item in items:
                if item.getName() == ingredient.getName():
                    if item.getIndicator() == "red":
                        print(f"{item.getName()} is running low, please refill")
                        return False
                    if item.getQuantity() < ingredient.getQuantity():
                        isEnough = False
            
            if isEnough == False:
                print(f"{self.__name} cannot be prepared because {lackingIngredient} is not sufficient")
                return False
        return isEnough

    def getName(self):
        return self.__name
    def getIngredients(self):
        return self.__ingredients