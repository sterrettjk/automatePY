def displayInventory (inventory):
    totalItems = 0
    print("Inventory:")
    for i, q in inventory.items():
        print(i + " " + str(q)) 
        totalItems += q

    print("Total number of items: " + str(totalItems))

#It took forever to get this to work. I wrote the function, saved it, imported to an interactive session, then realized I needed to add .items() to make the dict unpackable.
#After making the change, I ran "import displayInventory" again then ran the function only to get the original error again.
#Hmm, this is exactly how the book does it...
#Much head-scratching later I somehow thought "what if import doesn't do anything if the module was already imported"
#And sure enough that was it. After importing importlib and reloading the displayInventory module I could finally pass it an inventory dict and have it printed out as I wanted.
#Lesson learned: Doing the "simple assignments" even when you feel you already know the subject material can lead to other lessons learned.
