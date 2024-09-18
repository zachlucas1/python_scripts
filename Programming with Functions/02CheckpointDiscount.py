#imports the date and time from the computer
import datetime

#asks user for input of subtotal
subtotal = float(input('Please enter the subtotal: '))

#turns the weekdays into numbers (Monday = 1, Tuesday =2)
weekday = datetime.datetime.now().isoweekday()

#constant discount and sales tax rates
discount_rate = 0.10
sales_tax_rate = 0.06

#if statement that checks if subtotal is above 50 and if it is a Tuesday or Wednesday
#it later applies it to the subtotal
if subtotal > 50 and (weekday == 2 or weekday == 3):
    discount = round(subtotal * discount_rate, 2)
    subtotal -= discount

#applies the sales tax and adds it to the subtotal and outputs the grand total
sales_tax = round(subtotal * sales_tax_rate, 2)
total = subtotal + sales_tax
print(f'Your final total is: ${total:.2f}')