def addToInventory(inventory, addItems):
    newInventory = inventory
    #Go through all of the items in addItems
    #for each item in the list addItems
    for item in addItems:
        #check if the listed item is in inventory create an entry defaulted to 0 if not
        newInventory.setdefault(item, 0)
        #increment the item count in inventory
        newInventory[item] += 1
    #return the updated inventory
    return newInventory