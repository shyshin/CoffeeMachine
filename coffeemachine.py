from item import Item
from ingredient import Ingredient
from beverages import Beverage
import time
class CoffeeMachine:
    def __init__(self,noOfOutlets):
        self.__noOfOutlets = noOfOutlets
        self.__menu = {}
        self.__time = 5
        
    def setItems(self,items):
        self.__items = items
        self.__capacity = {}
        for item in items:
            self.__capacity[item.getName()]=item.getQuantity()

    def addBeverageToMenu(self,beverage):
        self.__menu[beverage.getName()] = beverage
    
    def _consumeItems(self,beverage):
        time.sleep(self.__time)
        for item in self.__items:
            for ingredient in beverage.getIngredients():
                if item.getName() == ingredient.getName():
                    item.setQuantity(item.getQuantity()-ingredient.getQuantity())
                    if item.getQuantity() < 10:
                        item.setIndicator("red")
    def prepareBeverage(self,drink):
        if drink not in self.__menu:
            print(f"{drink} is not present in menu")
        beverage = self.__menu[drink]
        if beverage.checkIfEnoughIngredients(self.__items) == True:
            self._consumeItems(beverage)
            print(f"{drink} is prepared")
    
    def refillItem(self,itemName):
        fullQuantity = self.__capacity[itemName]
        for item in self.__items:
            if item.getName() == itemName:
                item.setQuantity(fullQuantity)
                item.setIndicator("green")
                print(f"Refilled {itemName}")
    def getOutlets(self):
        return self.__noOfOutlets
    def setOutlets(self,N):
        self.__noOfOutlets = N