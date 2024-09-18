###### Finding the Largest number ######
"""numbers = [42, 25, 18, 83, 23, 85, 38, 2]

largest_so_far = numbers[0]

for number in numbers:
    if number > largest_so_far:
        largest_so_far = number

print(f'The largest is: {largest_so_far}')"""

###### Finding the maximum price ######
"""shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

max_price = -1

for item in shopping_cart:
    price = item[1] #Price is the second part of the item

    if price > max_price: #New max price
        max_price = price

print(f'The maximum price is: {max_price}')"""

###### Finding maximum price and the item ######
"""shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

max_price = -1
max_product = ""

for item in shopping_cart:
    product_name = item[0] #Item is first part of item
    price = item[1] #Price is the second part of the item

    if price > max_price: 
        max_price = price #New max price
        max_product = product_name #New max product

print(f'The maximum price is: {max_price}')
print(f'The product with the maximum price is: {max_product}')"""

###### Finding Oldest age and the person ######
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 9999
youngest_name = ""

for person_line in people:
    parts = person_line.split()
    name = parts[0]
    age = int(parts[1])

    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print(f'The youngest person is: {youngest_name} with an age of {youngest_age}.')