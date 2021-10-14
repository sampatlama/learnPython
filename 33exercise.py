# find the total cost for the items of cart
n = int(input('Enter the number of items in cart? '))
price = 0
store = ''
for items in range(n):
    item = str(input('Enter the name of item in cart? '))
    cost = int(input('Enter the price of the item? '))
    price += cost
    for items in [item]:
        store += items
print(f'The item in the cart are {store}')
print(f'The total cost is {price}')
# the items are printed concatenately
# will change later is i know the algo.