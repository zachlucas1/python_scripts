with open('hr_system.txt') as f: #opens file
    for line in f: #reads each line in file
        
        clean_line = line.strip() #strips off whitespace
        parts = clean_line.split(' ') #splits line into parts based on a space

        #Each part saved into a variable
        name = parts[0]
        id_number = parts[1]
        title = parts[2]
        salary = float(parts[3])

        #calculates paycheck amount
        pay = salary / 24

        #engineers get an $1000 bonus
        if title.lower() == 'engineer':
            pay += 1000

        #outputs the data
        print(f'Name: {name}, (ID: {id_number}), {title} - ${pay:.2f}')