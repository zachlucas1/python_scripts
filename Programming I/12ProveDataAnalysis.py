#Title: 12 Prove Assignment - Data Analysis
#Author: Zach Lucas
#Description: Program iterates through a data file, displays lowest and highest life 
#expectancy, then prompts user to input a year to find average life expectancy. 

age_high = 0
age_low = 99999
name_high = ''
name_low = ''
year_high = ''
year_low = ''

#opens file
with open('life-expectancy.csv') as f:
    age_high = 0
    age_low = 99999
    name_high = ''
    name_low = ''
    year_high = ''
    year_low = ''
    
    for line in f:

        #Cleans and seperates lines into parts
        clean_line = line.strip()
        part = clean_line.split(',')
        country = part[0]
        code = part[1]
        year = int(part[2])
        expectancy = float(part[3])

        if expectancy > age_high:
            name_high = country
            age_high = expectancy
            year_high = year

        if expectancy < age_low:
            name_low = country
            age_low = expectancy
            year_low = year

    print()
    print(f'The country with the highest life expectancy is {name_high} in {year_high} with a life expectancy of {age_high} years.')
    print()
    print(f'The country with the lowest life expectancy is {name_low} in {year_low} with a life expectancy of {age_low} years. ')
    print()

#opens file
with open('life-expectancy.csv') as f:

    input_age_high = 0
    input_age_low = 99999
    input_name_high = ''
    input_name_low = ''
    input_year_high = ''
    input_year_low = ''
    i = 0
    average = 0

    user_choose = int(input('What year do you want to find the average life expectancy? '))
    
    for line in f:
        user_clean_line = line.strip()
        user_part = user_clean_line.split(',')
        user_country = user_part[0]
        user_code = user_part[1]
        user_year = int(user_part[2])
        user_expectancy = float(user_part[3])

        if user_choose == user_year:
            i += 1
            average = average + user_expectancy
            if user_expectancy < input_age_low:
                input_age_low = user_expectancy
                input_name_low = user_country
            if user_expectancy > input_age_high:
                input_age_high = user_expectancy
                input_name_high = user_country

average = average / i
print()
print(f'The average life expectancy for that year was: {average:.2f} years.')
print()