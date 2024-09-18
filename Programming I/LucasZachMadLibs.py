#Title: Mad Lib Generator
#Author: Zach Lucas
#Description: Program asks user to input various words to output
#it into a mad lib type story.

#Ask for various types of words for the Mad Lib
print('Please enter the following:')
print(' ')
adjective1 = input('Adjective: ')
animal = input('Animal: ')
verb1 = input('Verb: ')
exclamation = input('Exclamation: ')
verb2 = input('Verb: ')
verb3 = input('Verb: ')
verb4 = input('Verb: ')
adjective2 = input('Adjective: ')

#The output of the Mad Lib with users inputted words
print(' ')
print('Wow! You are such a great author. Your story is: ')
print(' ')
print('The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective1} {animal} {verb1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all')
print(f'I could think to do was to {verb2} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb3}')
print('right in front of my family. I said, "How dare you do that in front of my family!')
print(f'I then proceeded to {verb4} him and {adjective2} into a cage. He never bothered us again!')
print(' ')