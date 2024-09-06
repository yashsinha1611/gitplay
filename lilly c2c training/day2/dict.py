inventory = {}
 
def add_inventory(id, name):
    inventory[id] = name
 
def display_inventory():
    for id, name in inventory.items():
        print(str(id) + ":", name)
 
def update_inventory(id, name):
    if id in inventory:
        inventory[id] = name
    else:
        
        add_inventory(id, name)
        print("Doesn't exist, create a new entry")
 
 
add_inventory(1, "Pencil")
display_inventory()  
 
# update_inventory(1, "Pen")  
# display_inventory()  
 
 
# update_inventory(2, "Eraser")
# display_inventory()  