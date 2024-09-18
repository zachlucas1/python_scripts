#Name: Banking with multiple lists
#Author: Zach Lucas
#Description: User inputs multiple accounts and their balances. 
# It later will output them as lists and computes the total and averages.

print('Enter the names and balances of bank accounts (type: quit when done)')

banking_list = []
balance_list = []
account_name = ''

while account_name != 'quit':
    account_name = str(input('What is the name of this account? '))
    if account_name != 'quit':
        banking_list.append(account_name)
        balance = float(input('What is the balance? '))
        balance_list.append(balance)
print()

print('Account Information:')
total = 0
average = 0
for i in range(len(banking_list)):
    print(f'{banking_list[i].capitalize()} - ${balance_list[i]:.2f}')
    total += (balance_list[i])
    average = (total / (len(banking_list)))

print()
print(f'Total: ${total:.2f}')
print(f'Average: ${average:.2f}')