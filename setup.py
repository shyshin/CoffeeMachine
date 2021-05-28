from coffeemachine import CoffeeMachine
from ingredient import Ingredient
from beverages import Beverage
from item import Item
import json
import pickle
if __name__ == "__main__":
    with open('./sample_input.json') as f:
        data = json.load(f)
    machine_setup = data['machine']
    
    coffee_machine = CoffeeMachine(machine_setup['outlets']['count_n'])
    
    items = []
    for item in machine_setup['total_items_quantity']:
        items.append(Item(item,machine_setup['total_items_quantity'][item]))
    
    coffee_machine.setItems(items)

    for beverage in machine_setup['beverages']:
        ingredients = []
        for ingredient in machine_setup['beverages'][beverage]:
            ingredients.append(Ingredient(ingredient,machine_setup['beverages'][beverage][ingredient]))
        coffee_machine.addBeverageToMenu(Beverage(beverage,ingredients))

    print("Cofee Machine Setup Done")
    with open('coffee_machine.obj','wb') as coffee_machine_file:
        pickle.dump(coffee_machine,coffee_machine_file)
    
    print("Stored coffee machine in coffee_machine.obj file")