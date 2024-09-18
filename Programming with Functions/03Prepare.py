                ####    PREP VIDEOS ###
### LISTS ###

"""names = ['Christopher', 'Susan']
scores = []
scores.append(98) # Add new item to the end
scores.append(99)
print(names)
print(scores)
print(scores[1]) # Collections start at zero"""

### ARRAYS (^^^ only works with obove code ^^^)###

"""from array import array
scores = array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])"""

### COMMON OPERATIONS ###

"""names = ['Christopher', 'Susan']
print(len(names)) #get number of items
names.insert(0, 'Bill') #insert before index
print(names)
names.sort()
print(names)"""

### RANGES ###

"""names = ['Susan', 'Christopher', 'Bill', 'Justin']
presenters = names[1:3]
#start and end index, numbers start on the first bracket and go on the commas
#prints all the names and then christopher and bill

print(names)
print(presenters)"""

### DICTIONARIES ###
# your_dictionary = {
# key : value,
# key : value
#}

"""person = {'first': 'Christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])"""

"""bad_guys = {
    'daredevil': 'kingpin',
    'x-men': 'apocalypse',
    'batman': 'bane'
}
print(bad_guys['batman'])
print(bad_guys['x-men'])
print(bad_guys['daredevil'])"""

                ### 03 PREPARE CONCEPTS ###

### LISTS ###

"""# Create a list that contains five words.
colors = ["yellow", "red", "green", "yellow", "blue"]

# Print the element that is stored
# at index 2 in the colors list.
print(colors[2])

# Print the entire colors list.
print(colors)

# Create an empty list that will hold fabric names.
fabrics = []

# Add three elements at the end of the fabrics list.
fabrics.append("velvet")
fabrics.append("denim")
fabrics.append("gingham")

# Insert an element at the beginning of the fabrics list.
fabrics.insert(0, "chiffon")

# Get the index where velvet is stored in the fabrics list.
i = fabrics.index("velvet")

# Replace velvet with taffeta.
fabrics[i] = "taffeta"

# Remove the last element from the fabrics list.
fabrics.pop()

# Remove taffeta from the fabrics list.
fabrics.remove("taffeta")

# Get the length of the fabrics list and print it.
n = len(fabrics)
print(f"The fabrics list contains {n} elements.")

# Use a for loop to print each element in the list. Of
# course, the code in the body of a loop can do much
# more with each element than simply print it.
for element in fabrics:
    print(element)

# Use the built-in sum function to
# add all the numbers in a list.
costs = [25.49, 16.35, 75.0, 16.12]
total = sum(costs)
print(total)"""

### LISTS ###

"""# Create a dictionary with student IDs as
# the keys and student names as the values.
students = {
    "42-039-4736": "Clint Huish",
    "61-315-0160": "Michelle Davis",
    "10-450-1203": "Jorge Soares",
    "75-421-2310": "Abdul Ali",
    "07-103-5621": "Michelle Davis"
}

# Add an item to the dictionary.
students["81-298-9238"] = "Sama Patel"

# Get the number of items in the dictionary and print it.
n = len(students)
print(n)

# Print the entire dictionary.
print(students)

# Get a student ID from the user.
id = input("Enter a student ID: ")

# Check if the student ID is in the dictionary.
if id in students:
    # Lookup the student ID in the dictionary and
    # retrieve the corresponding student name.
    name = students[id]

    # Print the student name.
    print(name)
else:
    print("No such student")

# Use a for loop to print each key value pair in the
# dictionary. Of course, the code in the body of a loop can
# do much more with each key value pair than simply print it.
for key, value in students.items():
    print(key, value)"""

### CONVERTING BETWEEN LISTS AND DICTIONARIES ###

"""# Create a list that contains five student numbers.
numbers = ["42-039-4736", "61-315-0160",
        "10-450-1203", "75-421-2310", "07-103-5621"]

# Create a list that contains five student names.
names = ["Clint Huish", "Michelle Davis",
        "Jorge Soares", "Abdul Ali", "Michelle Davis"]

# Convert the numbers list and names list into a dictionary.
student_dict = dict(zip(numbers, names))

# Print the entire student dictionary.
print(student_dict)

# Convert the student dictionary into
# two lists named keys and values.
keys = list(student_dict.keys())
values = list(student_dict.values())

# Print both lists.
print(keys)
print(values)"""

### TEXT FILES AND CSV ###

"""import csv

# Open a file named txtfile.csv and store a reference
# to the opened file in a variable named infile.
with open("txtfile.csv", "rt") as infile:

    # Use the csv module to create a reader
    # object that will read from the opened file.
    reader = csv.reader(infile)

    # The first line of the CSV file contains column headings
    # and not information about a dental office, so this
    # statement skips the first line of the CSV file.
    next(reader)

    # Read each row one at a time as a list.
    for row in reader:

        # For the current row, retrieve the
        # values in columns 0, 1, and 2.
        company = row[0]
        address = row[1]
        phone = row[2]

        # Print the values for the user to see.
        print(company, address, phone)"""

"""import csv

# Create an empty dictionary that will
# store the data from the CSV file.
dentists = {}

# Open a file named dentists.csv and store a reference
# to the opened file in a variable named infile.
with open("dentists.csv", "rt") as infile:

    # Use the csv module to create a reader
    # object that will read from the opened file.
    reader = csv.reader(infile)

    # The first line of the CSV file contains column headings
    # and not information about a dental office, so this
    # statement skips the first line of the CSV file.
    next(reader)

    # Read each row one at a time as a list.
    for row in reader:

        # For the current row, retrieve the
        # values in columns 0, 1, and 2.
        company = row[0]
        address = row[1]
        phone = row[2]

        # Store the data from the current row into the dentists
        # dictionary. Use the phone number as the key. Create a
        # list with the company name and address as the value.
        dentists[phone] = [company, address]

# Print the entire dentists dictionary.
print(dentists)"""