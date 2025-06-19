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
        key = parts[0].lower()
        try:
            value = int(parts[1]) #treats as integer
        except ValueError:
            try:
                value = float(parts[1]) #treats as float
            except:
                value = parts[1] ##treats as otherwise
        itemList.append((key, value))  # Store a tuple of (category, amount)

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

def display_category(name, category_dict):
    print(f"For {name.capitalize()}:")
    if category_dict:
        for item, values in category_dict.items():
            print(item, values)
    else:
        print(f"No {name} items were recorded...")


#considering the food  
display_category("food", food)

#considering the transportation 
display_category("transportation", transport)

#considering the bills
display_category("bills", bills)

#considering the entertainment   
display_category("entertainment", entertainment)

#considering the books  
display_category("books", books)

#considering the unavailable items in our list
display_category("Items we don't have in our category:", unavailableListItem)

print("\n\nFinished processing the details...")

