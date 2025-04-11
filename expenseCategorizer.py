# assuming these are the available list of items we can compare with
# "food", "transport", "bills", "books", "entertainment"
food ,entertainment, transport, bills, books = {}


# Get the number of items
while True:
    noItems = input("Enter the number of items>> ")
    try:
        noItems = int(noItems) #tries to cast the result into an int
        break
    except ValueError:
        print("Ensure your input value is an integer number!!!")

# Store the list of items
itemList = {}
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
    else:
        print("Ensure you enter data using the correct format...\n (e.g orange 50) where 'orange' is the item and '50' is the cost")
    
    itemList[key] = value

    currentIndex = currentIndex + 1


# Classifying the user item list
currentIndex = 0
unavailableListItem = {}
for item in itemList:
    if str(item) == "food":
        food[item] = itemList[item]
    elif str(item) == "transport":
        transport[item] = itemList[item]
    elif str(item) == "bill":
        bills[item] = itemList[item]
    elif str(item) == "book":
        books[item] = itemList[item]
    elif str(item) == "entertainment":
        entertainment[item] = itemList[item]
    else:
        unavailableListItem[item] = itemList[item]


print(food)
print(books)
print(unavailableListItem)