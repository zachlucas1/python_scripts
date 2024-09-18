age_high = 0
age_low = 99999
name_high = ''
name_low = ''
year_high = ''
year_low = ''

#opens file
with open('life-expectancy.csv') as f:
    
    for line in f:

        #Cleans and seperates lines into parts
        clean_line = line.strip()
        part = clean_line.split(',')
        country = part[0]
        code = part[1]
        year = int(part[2])
        expectancy = float(part[3])

        if expectancy > age_high:
            age_high = expectancy
        if expectancy < age_low:
            age_low = expectancy

    print()
    print(f'The highest life expectancy is: {age_high}, and the lowest is: {age_low}.')
    print()