#module that picks at random and wraps text at a certain value
import random
import textwrap

#opens file
with open('quotes.txt' , 'rt') as infile:

    #reads each line so they can be seperated later
    lines = infile.readlines()

    #print(lines)

    #ask user how many quotes they want
    amount = int(input('How many quotes do you want? '))
    print('')

    for i in range(amount):
        #picks a random quote from the file
        choice = random.choice(lines)

        #Automatically textwraps at 70 charachters
        choice_wrap = textwrap.wrap(choice, width = 70)

        #prints the statement
        #the \n gets rid of the brackets and make it looks better overall
        print('\n'.join(choice_wrap))
        print('')

        #this will just print the author names
        #to make it work add .split('-') to line 19 and comment out 22, 26, and 27 
        #author = choice[1]
        #print(author)