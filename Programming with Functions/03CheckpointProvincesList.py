#opens the file as txt file
with open('provinces.txt', 'rt') as txtfile:

    #Reads all lines into a list named provinces. Each line will be stored in
    #its own element
    string = txtfile.read()
    provinces = string.splitlines()

#prints entire list
print(provinces)

#removes first element of list
provinces.pop(0)
#print(provinces)

#remove the last element of the list
provinces.pop()
#print(provinces)

#Replace all occurences of "AB" in the list with "Alberta"
# for i in range(len(provinces)):
#     if provinces[i] == "AB":
#         provinces[i] == "Alberta" 
# (for some reason this ^^^ didnt work and I had to change it to this VVV)
while 'AB' in provinces:
    abbreviation = provinces.index('AB')
    provinces[abbreviation] = 'Alberta'
#print(provinces)

#Count the number of 'Alberta' and print that number
count = 0
for province in provinces:
    if province == 'Alberta':
        count += 1

print()
print(f'Alberta occurs {count} times in the modified list')
