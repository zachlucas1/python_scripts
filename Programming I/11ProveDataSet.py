high = 0
low = 100

with open('life-expectancy.csv') as f: #opens file
    for line in f:

        clean_line = line.strip() #strips off whitespace
        parts = clean_line.split(',')

        country = parts[0]
        code = parts[1]
        year = parts[2]
        life_expectancy = float(parts[3])

        for line in parts:
            if life_expectancy > high:
                high = life_expectancy
            if life_expectancy < low:
                low = life_expectancy

    print(f'The highest life expectancy is: {high}.')
    print(f'The lowest life expectancy is: {low}.')
        #print(parts)