#Imports random number generator for the game
import random
number = random.randint(1, 10)
#print(number)

#Gets users input and compares it to random number
print( )
guess_number = int(input('What is your guess? '))

while guess_number != number:
    if guess_number > number:
        print('Lower')
        guess_number = int(input('What is your guess? '))
    elif guess_number < number:
        print('Higher')   
        guess_number = int(input('What is your guess? '))
print('You guessed it!')