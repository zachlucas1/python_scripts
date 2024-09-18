import csv

#empty dictionary that will store student info
students = {}

#opens file
with open('pupils.csv', 'rt') as infile:
    
    #this will read the file
    reader = csv.reader(infile)
    
    #skips the first line
    next(reader)

    #read each row as a list
    for row in reader:

        #retrieve values in columns 0 and 1
        inumber = row[0]
        name = row[1]

        #add students i number and name to dictionary
        students[inumber] = name

#gets input from user
inumber_input = str(input('Please enter an I-Number (xx-xxx-xxxx): '))

#removes dashes from users input
inumber_input = inumber_input.replace('-', '')

#see if user input is formatted correctly
if inumber_input.isdigit():
    if len(inumber_input) < 9:
        print('Invalid I-Number: too few digits')
    elif len(inumber_input) > 9:
        print('Invalid I-Number: too many digits')
    else:
        #if user input is correct find the i number in list
        if inumber_input in students:
            
            #retrieve the name from the correct input
            name = students[inumber_input]
            print(name)
        else:
            print('No such student')
else:
    print('Invalid charachter in I-Number')