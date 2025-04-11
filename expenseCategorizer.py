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
itemList = defaultdict(list)
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
unavailableListItem = defaultdict(list)
for item in itemList:
    if str(item) == "food":
        food[item].append(itemList[item])
    elif str(item) == "transport":
        transport[item].append(itemList[item])
    elif str(item) == "bill":
        bills[item].append(itemList[item])
    elif str(item) == "book":
        books[item].append(itemList[item])
    elif str(item) == "entertainment":
        entertainment[item].append(itemList[item])
    else:
        unavailableListItem[item].append(itemList[item])


#displaying the result for the categoried expenses
print("\nThe categorized expenses of the user include:")

#considering the food  
print("For Food:")
if len(food) > 0:
    for foodItem in food:
        print(foodItem, food[foodItem])
else:
    print("No food was recieved...")

# #considering the transportation
# print("For transportation:")    
# if len(transport) > 0:
#     for transportItem in transport:
#         print(transportItem, transport[transportItem])
# else:
#     print("No transportation Item was recorded...")

# #considering the bills
# print("For bills:")   
# if len(bills) > 0:
#     for bill in bills:
#         print(bill, bills[bill])
# else:
#     print("No bills were recorded...")

# #considering the entertainment
# print("For entertainment:")   
# if len(entertainment) > 0:
#     for ent in entertainment:
#         print(ent, entertainment[ent])
# else:
#     print("No entertaiment Item was recorded...")

# #considering the books  
# print("For books:") 
# if len(books) > 0:
#     for book in books:
#         print(book, books[book])
# else:
#     print("No books were recorded...")

# #considering the unavailable items in our list
# print("For Items we don't have in out category:") 
# if len(unavailableListItem) > 0:
#     for item in unavailableListItem:
#         print(item, unavailableListItem[item])

# print("\n\nFinished processing the details...")

print(food)