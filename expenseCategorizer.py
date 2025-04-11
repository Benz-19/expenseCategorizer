from collections import defaultdict

# assuming these are the available list of items we can compare with
# "food", "transport", "bills", "books", "entertainment"
food  = defaultdict(list)
entertainment = defaultdict(list) 
transport = defaultdict(list)
bills = defaultdict(list)
books = defaultdict(list)


# Get the number of items
while True:
    noItems = input("Enter the number of items>> ")
    try:
        noItems = int(noItems) #tries to cast the result into an int
        break
    except ValueError:
        print("Ensure your input value is an integer number!!!")

# Store the list of items
itemList = []
currentIndex  = 0

print("\nEnter the items in the format (e.g orange 50) where 'orange' is the item and '50' is the cost:")
while  currentIndex < noItems:
    print("Item ", str(currentIndex + 1) + " = ")
    inputPair = input()
    parts = inputPair.split()

    if len(parts) == 2:
        key = parts[0]
        try:
            value = int(parts[1]) #treats as integer
        except ValueError:
            try:
                value = float(parts[1]) #treats as float
            except:
                value = parts[1] ##treats as otherwise
        itemList.append((key, value))  # Store (key, value) tuple

    else:
        print("Ensure you enter data using the correct format...\n (e.g orange 50) where 'orange' is the item and '50' is the cost")
    
    currentIndex = currentIndex + 1


# Classifying the user item list
currentIndex = 0
unavailableListItem = defaultdict(list)
for key, item in itemList:
    if key == "food":
        food[key].append(item)
    elif key == "transport":
        transport[key].append(item)
    elif key == "bill":
        bills[key].append(item)
    elif key == "book":
        books[key].append(item)
    elif key == "entertainment":
        entertainment[key].append(item)
    else:
        unavailableListItem[key].append(item)


#displaying the result for the categoried expenses
print("\nThe categorized expenses of the user include:")

#considering the food  
print("For Food:")
if food:
 for foodItem, foodValues in food.items():
        print(foodItem, foodValues)
else:
    print("No food was recieved...")

#considering the transportation
print("For transportation:")    
if transport:
    for transportItem, transport in transport.items():
        print(transportItem, transport)
else:
    print("No transportation Item was recorded...")

#considering the bills
print("For bills:")   
if bills:
    for bill, bills in bills.items():
        print(bill, bills)
else:
    print("No bills were recorded...")

#considering the entertainment
print("For entertainment:")   
if entertainment:
    for ent, entertainment in entertainment.items():
        print(ent, entertainment)
else:
    print("No entertaiment Item was recorded...")

#considering the books  
print("For books:") 
if books:
    for book, books in books.items():
        print(book, books)
else:
    print("No books were recorded...")

#considering the unavailable items in our list
print("For Items we don't have in out category:") 
if unavailableListItem:
    for item, unavailableListItem in unavailableListItem.items():
        print(item, unavailableListItem)

print("\n\nFinished processing the details...")

