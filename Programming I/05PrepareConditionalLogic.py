color = input('What is your favorite color? ')

#outputs colors depending on input
if color.lower() == 'red':
    print('I like red too.')
elif color.lower() == 'green':
    print('I like green too.')
elif color.lower() == 'blue':
    print('I like blue too.')
elif color.lower() == 'yellow':
    print('I like yellow too.')
elif color.lower() == 'orange':
    print('I like orange too.')

#If it cannot find a color it outputs this statement
else:
    print('I have never heard of that color.')
