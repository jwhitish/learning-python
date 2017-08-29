#turns a list of strings into a dictionary

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
myInventory = {}

def addToInventory(inventory, addedItems):
  #inventory is dictionary, addedItems is a list
  for i in addedItems:
    inventory.setdefault(i, 0)
    inventory[i] = inventory[i] + 1
  print inventory


addToInventory(myInventory, dragonLoot)
