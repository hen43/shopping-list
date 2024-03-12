global choice
choice = 0
stopProject = 0
items = []

# TEST LIST

items.append({
  'name': 'Fortnite Burger', 
  'quantity': 9001, 
  'price': 32.32
})

items.append({'name': 'Burger King Foot Lettuce', 'quantity': 15, 'price': 0.01})

# VERY EPIC GUIDE ON USING DICTIONARIES

# def addItem(name, quantity, price):
#     items.append({'name': name, 'quantity': quantity, 'price': price})
#     items.append({'name': 'Forrnite Man', 'quantity': 9001, 'price': 12398})
  
# addItem('poop', 123, 23.2)
# print(items)
# print(items[1]['name']) -----------> returns names of the 2nd items 

def viewList():
  for i in items:
    print(f'''
Item: {i['name']}
Quantity: {i['quantity']}
Price: ${i['price']}
    ''')

def removeItem(item):
  items.pop(item)

def navigate(choice):
  if choice == 0:
    try:
      choice = int(input('''
SHOPPING LIST

[1] Add Item
[2] Remove Item
[3] View List

'''))
    except ValueError:
      print('that aint an option bubba')
    if choice == 1: # ADD ITEM TO LiST
      name = input('what\'s the item name??')
      quantity = int(input('how many are you buying?'))
      price = float(input('how much does it cost in dollars?'))

      items.append({
        'name': name, 
        'quantity': quantity, 
        'price': price,
      })
    elif choice == 2: # REMOVE ITEM FROM LIST
      remove = int(input('which item to remove????'))
      removeItem(remove)
    elif choice == 3: # VIEW LIST
      viewList()
    else:
      navigate(choice)

while stopProject == 0:
    navigate(choice)
