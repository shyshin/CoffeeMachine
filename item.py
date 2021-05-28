from ingredient import Ingredient


class Item(Ingredient):
    def __init__(self,name,quantity):
        super().__init__(name,quantity)
        self.__indicator = "green"
    
    def getIndicator(self):
        return self.__indicator
    
    def setIndicator(self,indicator):
        self.__indicator = indicator
