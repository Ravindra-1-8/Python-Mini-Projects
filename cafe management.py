# Python Mini Projects 1: CAFE MANAGEMENT
# step 1: Greeting the user.
# step 2: Showing Menu {'pizza': 50, 'salad': 30, 'burger' : 100, 'pop corn': 150}
# step 3: note the items.
# step 4: Check the item in our menu.
#           if Yes: add the cost
#                Ask user for anything else
#                     if yes: note the second item
#                            Check the item in our menu
#                                 calculate total cost & display
#                     if No: End order & display cost
#           if No: display error message.

menu = {'pizza': 250, 'salad': 150, 'burger' : 150, 'pop corn': 100 }

print("Welcome to our Lavish cafe.")
print("'pizza': 250,\n'salad': 150,\n'burger': 150,\n'pop corn': 100.\n")

order_item = input("What would you like to have Sir/Madam: ")

order_total  = 0

if order_item in menu:
    order_total += menu[order_item]
    order = input("Do you have anything else (Yes/No): ")

    if order == 'Yes':
        order_item2 = input("What would you like to be your second choice: ")

        if order_item2 in menu:
            order_total += menu[order_item2]
            print(f"Your total order value is: {order_total}")
    else:
        print(f"Your total order value is: {order_total}")

else:
    print("Sorry, we don't have that item.")