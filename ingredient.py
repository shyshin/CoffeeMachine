

class Ingredient:

    def __init__(self,name,quantity):
        self.__quantity = quantity
        self.__name = name

    def setQuantity(self,quantity):
        self.__quantity = quantity

    def getQuantity(self):
        return self.__quantity
    
    def getName(self):
        return self.__name