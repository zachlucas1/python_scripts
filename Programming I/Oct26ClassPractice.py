#is_debug_containers = True
is_debug_containers = False
if is_debug_containers:
    
    #Default conversion, cup runth over
    myFloat = 3.14
    myInt = int(myFloat)
    myBoolean = bool(myInt)

    print(f'float {myFloat} int {myInt} bool {myBoolean}')
    #By updating myFloat we did not update myInt, or myBoolean
    myFloat = 0.12345
    print(f'float {myFloat} int {myInt} bool {myBoolean}')

#LISTS
#is_debug_lists = True
is_debug_lists = False
if is_debug_lists:
    string_list = ['Matthew', 'Mark', 'Luke', 'John', 'Mary', 'Sarah']
    print(f'{string_list}')
    number_list = [0, 2, 1, 3.14, 5]
    print(f'{number_list}')

#Starting out with empty list and then adding
empty_list = []

#is_dictionary = True
is_dictionary = False
if is_dictionary:
    
    #Define the keys
    key_first = 'first'
    key_last = 'last'

    #Declaring & Initializing
    my_name_dictionary1 = {key_first: 'Bro.', 'last':'Clements'}
    print(my_name_dictionary1)

    my_name_dictionary2 = {}
    print(my_name_dictionary2)
    my_name_dictionary2[key_first] = 'Bro.'
    my_name_dictionary2[key_last] = 'Burton'
    print(my_name_dictionary2)
    if key_first in my_name_dictionary2: print('Yeh')

    teachers = [my_name_dictionary1, my_name_dictionary2
                {key_first: 'Bro.', key_last: 'Macbeth', 'Title': 'SW Engr'}]
print(len(teachers))
for teachers in teachers
print(teacher)
print(f'{teacher[key_first] {teacher['last']}is a great teacher')

###LOOPS###
is_debug_for = False
is_debug_for_numbers = False
is_debug_for_string = False
is_debug_for_num_range = False

#Container for numbers
is debug_for_numbers = True
if debug_for_numbers:
    number_list = [1, 2, 3, 4]
