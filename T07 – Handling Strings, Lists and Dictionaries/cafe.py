menu=['Burger','chips','Hotdog','Tea']  # Create a list called menu contain four items sold in the café.

# create a dictionary called stock contain the stock value for each item on the menu
stock = {
    'Burger':5,
    'chips':5,
    'Hotdog':5,
    'Tea':5
}

# Create dictionary called price contain the prices for each item on the menu
price = {
    'Burger':4,
    'chips':3,
    'Hotdog':2,
    'Tea':1
}

# calculate the worth of the total_stock in the café
total_stock=0
for i in range(len(menu)): 
    item_value = (stock[menu[i]] * price[menu[i]])
    total_stock += item_value

# Print out the result
print(f'The worth of the total_stock in the café is ${total_stock}')