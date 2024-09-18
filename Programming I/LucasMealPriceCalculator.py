#Title: Meal Price Calculator
#Author: Zach Lucas
#Description: User inputs meal prices, people, tax rate
#and tip, and outputs a total. Later it asks for payment
#amount and outputs the change. 

#Asks user for input of prices, people, and sales tax
child_meal = float(input('What is the price of a child\'s meal? '))
adult_meal = float(input('What is the price of an adult\'s meal? '))
children = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))
sales_tax_rate = float(input('What is the sales tax rate? ')) 
tip = float(input('What is the tip amount? '))
print(' ')

#Subtotal math
child_subtotal = float(child_meal * children)
adult_subtotal = float(adult_meal * adults)
subtotal = float(child_subtotal + adult_subtotal)

#Sales tax math
sales_tax = (sales_tax_rate / 100)
tax = float(sales_tax * subtotal)

#Output totals
print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax * subtotal:.2f}')
print(f'Tip: ${tip:.2f}')
print(f'Total: ${subtotal + tax + tip:.2f}')
print(' ')
payment = float(input('What is the payment amount? '))

#Payment math
change = payment - (subtotal + tax + tip)
print(' ')

print(f'Change: ${change:.2f}')