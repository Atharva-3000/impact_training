# write a program to manage the inventory of a store
# inventory: print the items id, name, quantinty and price of the items in the inventory
# buying from vendor: vendor input id and quantity, price and update the inventory
#selling to customer: ask for id/name, quantity and update the inventory
# search by id: search the item by id and display the details
# exit


inventory = {}
while True:
    print("1. Inventory")
    print("2. Buying from vendor")
    print("3. Selling to customer")
    print("4. Search by id")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("ID\tName\tQuantity\tPrice")
        for i in inventory:
            print(i, end="\t")
            for j in inventory[i]:
                print(j, end="\t")
            print()
    elif choice == 2:
        id = input("Enter id: ")
        name = input("Enter name: ")
        quantity = int(input("Enter quantity: "))
        price = int(input("Enter price: "))
        inventory[id] = [name, quantity, price]
    elif choice == 3:
        id = input("Enter id: ")
        name = input("Enter name: ")
        quantity = int(input("Enter quantity: "))
        if id in inventory:
            if inventory[id][1] >= quantity:
                inventory[id][1] -= quantity
            else:
                print("Not enough quantity")
        else:
            print("Item not found")
    elif choice == 4:
        id = input("Enter id: ")
        if id in inventory:
            print("ID\tName\tQuantity\tPrice")
            print(id, end="\t")
            for j in inventory[id]:
                print(j, end="\t")
            print()
        else:
            print("Item not found")
    elif choice == 5:
        break
    else:
        print("Invalid choice")
    print()
           