"""if price >= 1.00:
    tax = .07
else:
    tax = 0
    print(tax)"""

"""country = 'CANADA'
if country.lower() == 'canada'
   print('oh look a canadian')"""

"""country = input('Enter the name of your home country: ')
if country.lower() == 'canada':
    print('So you must like hockey!')
else:
    print('You are not from Canada')"""

province = input('What Province do you live in? ')
tax = 0

if province.lower() in ('alberta','nunavut','yukon'):
    tax = 0.05
elif province.lower() == 'ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)
