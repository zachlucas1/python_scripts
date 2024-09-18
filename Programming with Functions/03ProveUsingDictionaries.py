import csv
import pprint #makes it look nicer when printing

#empty dictionary
grocery_list = {}

print('')
print('Products')

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
        product_item = row[1]
        product_price = float(row[2])

        #store data in grocery_list dictionary
        grocery_list[product_key] = [product_item, product_price]

pprint.pprint(grocery_list)
print('')


print('Requested Items')

#for the request.csv file
requested_item = {}

#read the request.csv file into a dictionary
with open('request.csv', 'rt') as infile2:
    
    #reads the file
    request_reader = csv.reader(infile2)

    #skips the first line
    next(request_reader)

    #reads each row into a list
    for row in request_reader:
        request_key = row[0]
        requested_quantity = row[1]

        requested_item = grocery_list[request_key]
        item_name = requested_item[0]
        item_price = requested_item[1]

        print(f'{item_name}: {requested_quantity} @ {item_price}')
print('')