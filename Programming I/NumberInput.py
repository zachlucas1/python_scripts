#Ask for input of age
age = int(input('How old are you? '))

#Output age + 1
print(f'On your next birthday you will be {age + 1}')
print(' ')

#Ask for input of the number of egg cartons
egg = int(input('How many egg cartons do you have? '))

#Output the number of eggs
print(f'You have {egg * 12} eggs')
print(' ')

#Ask for input on cookies
cookies = int(input('How many cookies do you have? '))
people = int(input('How many people are there? '))
CookiesPerPerson = cookies / people

#Output number of cookies per person
print(f'Each person may have {CookiesPerPerson} cookies')
print(' ')