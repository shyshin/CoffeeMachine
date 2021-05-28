import pickle
import sys
if __name__ == "__main__":
    with open('coffee_machine.obj','rb') as coffee_machine_file:
        coffee_machine = pickle.load(coffee_machine_file)
    
    N = coffee_machine.getOutlets()
    
    if N <= 0:
        print ("Machine running at full capacity")
        sys.exit()
    N -= 1
    coffee_machine.setOutlets(N)
    with open('coffee_machine.obj','wb') as coffee_machine_file:
        pickle.dump(coffee_machine,coffee_machine_file)
    
    query = input()
    while query != "exit":
        query_lst = query.split(' ')
        if query_lst[0]=="prepare_beverage":
            drink = query_lst[1]
            coffee_machine.prepareBeverage(drink)
        elif query_lst[0]=="refill_item":
            itemName = query_lst[1]
            coffee_machine.refillItem(itemName)
        query = input()
    
    with open('coffee_machine.obj','rb') as coffee_machine_file:
        coffee_machine = pickle.load(coffee_machine_file)
    
    N = coffee_machine.getOutlets()
    coffee_machine.setOutlets(N+1)
    with open('coffee_machine.obj','wb') as coffee_machine_file:
        pickle.dump(coffee_machine,coffee_machine_file)
    