#Asks user for input of height and age
first_rider_age = int(input('What is the age of the first rider? '))
first_rider_height = int(input('What is the height of the first rider? '))
second_rider_question = str(input('Is there a second rider (yes/no)? ')).lower()

if second_rider_question == 'yes':
    second_rider_age = int(input('What is the age of the second rider? '))
    second_rider_height = int(input('What is the height of the second rider? '))
    if (second_rider_age >= 18 or first_rider_age >= 18) and (first_rider_height >= 36 or second_rider_height >= 36):
        print('You may ride.')
    else:
        print('Sorry, You may not ride.')

else:
    if first_rider_age >= 18 and first_rider_height >= 62:
        print('You may ride.')
    else:
        print('Sorry, You may not ride.')