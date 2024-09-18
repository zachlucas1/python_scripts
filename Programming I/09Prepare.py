### 09 PREPARE LISTS ###
"""clients = []

clients.append("Emily")
clients.append("John")
clients.append("Mary")

for client in clients:
    print(client)"""

#-------------------------------

clients = []

new_client = ""
while new_client != 'quit':
    new_client = input('What is the name of the client? ')
    clients.append(new_client)

for client in clients:
    print(clients)

#-------------------------------

"""friends = ['Luc', 'Kristi', 'Rex']
tips = [12.25, 13.95, 8.50]

running_total = 0

for tip_amount in tips:
    #running_total = running_total + tip_amount (Use this or the one below to calculate)
    running_total += tip_amount

print(f'The total is: {running_total:.2f}')"""

#-------------------------------