#Title: Grocery List
#Author: Zach Lucas
#Description: User uses a menu to add items, view cart, remove them, and compute the
#total while shopping. It then will display these elements. 

#Intro
print()
print('Welcome to your personal grocery list assistant!')
print()

shopping_list = []
price_list = []
action = 0
quantity = ''
index = 0

while action != 5:

#The main menu for the user
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    print()

    action = int(input('Please enter an action: '))
    print()

    if action == 1: #Add item
        item = input('What item would you like to add? ').capitalize()
        shopping_list.append(item)
        price = float(input(f'What is the price of "{item}"? '))
        price_list.append(price)
        print(f'"{item}" has been added to your cart')
        print()

    elif action == 2: #View cart
        print('Here are the items on your list: ')
        for i in range (len(shopping_list)):
            print(f'{(i+1)}. {shopping_list[i]} - ${(price_list[i])}')
        print()

    elif action == 3: #Remove item
            remove_item = int(input('What item number would you like to remove? '))
            remove_item -= 1
            length_shopping_list = (len(shopping_list))
            shopping_list.pop(remove_item)
            price_list.pop(remove_item)
            print(f'{item} has been removed from the shopping list')
            if index > length_shopping_list:
                print('That is not a valid number')

    elif action == 4: #Compute total
        total = 0
        for i in price_list:
            total += i
        print(f'The total of your shopping cart is: ${total:.2f}')

    elif action == 5: #quit program
        print('Thank you, goodbye.')

    else:
        print('Sorry, that is not a valid item number.')
        print()
        action = input('Please enter an action: ')