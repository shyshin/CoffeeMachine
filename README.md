The coffee machine design requires designing coffee machine with multiple outlets (N).

Keeping that in mind, I have segregated the problem into 2 tasks:
1- Setup the coffee machine.
2- Query the coffee machine.

### For Setup of coffee machine:
Run the following:
``` 
    python3 setup.py
```

This will take input from sample_input.json file and create a coffeemachine object. This is object is then serialized into a file: coffee_machine.obj .

### For Query of Coffee Machine:

We dont want more than N process querying the COffee machine. For this, I have implemented a semaphore which decreases the no of outlets value every time a process is run. If the no of outlets is 0, the process is halted.

you can run the runner.py:
```
    python3 runner.py

```
3 queries can be given:

   1. prepare_beverage <beverage_name>

This will prepare the beverage after checking if coffee machine items are sufficient to fulfill this request. If indicator is red for an item, error would raised indicating which item requires refill.
   2. refill_item <item_name>

Refill item to the original capacity
   3. exit

Exit the program
