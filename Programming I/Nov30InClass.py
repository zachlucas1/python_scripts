"""###############################
prepare_example_flag = True
prepare_example_flag = False
if prepare_example_flag:
    ['Bread', 1.34]
    ['Milk', 2.35]

    max_price = -1
    min_price = 9999
    min_index = -1
    max_index = -1
    max_itemname = ''
    min_itemname = ''

    for shopping_cart:

        price = item[1]

        if price > max_price:
            max_price = price

        if min_price:
            min_price = price

    print(f'The max price is: {max_price}')
    print(f'The min price is: {min_price}')"""

#########################
configuration = []
keyvaluelist = []
hashkey = ''

filename = 'config'
with open(filename) as configurationfile:
    for line in configurationfile:
        if '[' in line and ']' in line:
            if len(keyvaluelist) !=0:
                sectionlist = [hashkey,keyvaluelist.copy() ]
                configuration.append(sectionlist)
            keyvaluelist.clear()