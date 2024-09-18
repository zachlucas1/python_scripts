###FOR LOOPS AND WHILE LOOPS###

#Print text as a list
"""for name in ['Christopher', 'Susan']:
    print(name)"""

#Print numbers as a list starting from 0-2
"""for index in range (0, 2):
    print(index)"""

#While loop
"""names = ['Christopher', 'Susan']
index = 0
while index < len(names):
    print(names[index])
    #Change the condition
    index = index + 1"""

#Comparing For and While loops (They both display the same thing)
"""people = ['Christopher', 'Susan']

#For loop
for name in people:
    print(name)

#While loop
index = 0
while index < len(people):
    print(people[index])
    index = index + 1"""

#Lists
"""items = ['crayon', 'scissors', 'paper', 'glitter glue', 'markers', 'pens']
for item in items:
    print(f'The item is: {item}')"""

#Looping through numbers
"""for number in range(10, 20):
    print(number)"""

###Looping until something happens###
number = 0

while number < 10:
    number = int(input('What is the number? '))

#It displays this once you input a number greater than 10
print('Finished with the loop.')