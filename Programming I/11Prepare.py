with open('11preparetextfile.txt') as courses_file:
    for line in courses_file:
        # line = "CSE 110,98.5"
        clean_line = line.strip()
        print(clean_line)

        # parts = line.split(',')

        # # parts = ["CSE 110", "98.5"]
        # name = parts[0]
        # grade = float(parts[1])
        
        # bonus_grade = grade + 3

        # print(f'{name} - Grade: {grade}, after bonus: {bonus_grade}')




######

"""colors = 'red,green,blue,yellow'

color_parts = colors.split('e')

print (colors)
print(color_parts)

for color in color_parts:
    print(color)

second = color_parts[1]
print(second)"""

######

"""name = '\tZach Lucas      \n'

#clean_name = name.strip()
name = name.strip()

print(f'----{name}----')
#print(f'----{clean_name}----')"""