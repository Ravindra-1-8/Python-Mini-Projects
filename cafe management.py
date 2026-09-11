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

menu = {'pizza': 50, 'salad': 30, 'burger' : 100, 'pop corn': 150 }

print("Welcome to our Lavish cafe.")
print("'pizza': 50,\n'salad': 30,\n'burger': 100,\n'pop corn': 150.\n")

order_item = input("What would you like to have Sir/Madam: ")

order_total  = 0

if order_item in menu:
    order_total += menu[order_item]
print(order_total)