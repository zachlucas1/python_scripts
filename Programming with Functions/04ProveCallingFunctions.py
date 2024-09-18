"""This is Bro. Falin's solution"""
import csv
import pprint #makes it look nicer when printing
import datetime #gets current date and time from operating system

current_date_and_time = datetime.datetime.now()
date_and_time = current_date_and_time.strftime('%A, %B %dth %Y %I:%M %p')

#empty dictionary
grocery_list = {}

# print('')
# print('Products')

#open products.csv and store content into grocery_list dictionary
with open('products.csv', 'rt') as infile1:

    #this will read the file
    products_reader = csv.reader(infile1)
    
    #skips the first line because it contains a heading we dont need
    next(products_reader)

    #read each row as a list
    for row in products_reader:

        #retrieve values in columns 0-2
        product_key = row[0]
        product_name = row[1]
        product_price = float(row[2])

        #store data in grocery_list dictionary
        grocery_list[product_key] = [product_name, product_price]

# pprint.pprint(grocery_list)
# print('')

print('Inkom Emporium')
print('')

#for the request.csv file
requested_item = {}

#read the request.csv file into a dictionary
with open('request.csv', 'rt') as infile2:
    
    #reads the file
    request_reader = csv.reader(infile2)

    #skips the first line
    next(request_reader)

    number_of_items = 0
    subtotal = 0

    #reads each row into a list
    for row in request_reader:
        request_key = row[0]
        requested_quantity = int(row[1])

        requested_item = grocery_list[request_key]
        item_name = requested_item[0]
        item_price = requested_item[1]

        print(f'{item_name}: {requested_quantity} @ {item_price}')

        #calculate things
        number_of_items = number_of_items + requested_quantity
        subtotal = subtotal + (requested_quantity * item_price)
        sales_tax = subtotal * 0.06

#prints out the receipt, date, and time
print('')
print(f'Number of Items: {number_of_items}')
print(f'Subtotal: ${subtotal}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${subtotal + sales_tax:.2f}')

print('')
print('Thank you for shopping at the Inkom Emporium')
print(f'{date_and_time}')
print('')


"""This is my solution"""
# import csv
# import pprint #makes it look nicer when printing
# import datetime #gets current date and time from operating system

# current_date_and_time = datetime.datetime.now()
# date_and_time = current_date_and_time.strftime('%A, %B %dth %Y %I:%M %p')

# #empty dictionary
# grocery_list = {}

# # print('')
# # print('Products')

# #open products.csv and store content into grocery_list dictionary
# with open('products.csv', 'rt') as infile1:

#     #this will read the file
#     products_reader = csv.reader(infile1)
    
#     #skips the first line because it contains a heading we dont need
#     next(products_reader)

#     #read each row as a list
#     for row in products_reader:

#         #retrieve values in columns 0-2
#         product_key = row[0]
#         product_name = row[1]
#         product_price = float(row[2])

#         #store data in grocery_list dictionary
#         grocery_list[product_key] = [product_name, product_price]

# # pprint.pprint(grocery_list)
# # print('')

# print('Inkom Emporium')
# print('')

# #for the request.csv file
# requested_item = {}

# #read the request.csv file into a dictionary
# with open('request.csv', 'rt') as infile2:
    
#     #reads the file
#     request_reader = csv.reader(infile2)

#     #skips the first line
#     next(request_reader)

#     number_of_items = []
#     subtotal = []
#     #reads each row into a list
#     for row in request_reader:
#         request_key = row[0]
#         requested_quantity = int(row[1])

#         requested_item = grocery_list[request_key]
#         item_name = requested_item[0]
#         item_price = float(requested_item[1])

#         print(f'{item_name}: {requested_quantity} @ {item_price}')

#         #adds items in requested quantity to a list called number_of_items on line 53
#         number_of_items.append(requested_quantity)

#         #adds the total of item_price x requested_quantity to a subtotal list on line 54
#         subtotal.append(item_price * requested_quantity)

#         #gets the sum of the subtotal and multiplies it by 0.06
#         sales_tax = sum(subtotal) * 0.06

# #prints out the receipt, date, and time
# print('')
# print(f'Number of Items: {sum(number_of_items)}')
# print(f'Subtotal: ${sum(subtotal)}')
# print(f'Sales Tax: ${sales_tax:.2f}')
# print(f'Total: ${sum(subtotal) + sales_tax:.2f}')

# print('')
# print('Thank you for shopping at the Inkom Emporium')
# print(f'{date_and_time}')
# print('')