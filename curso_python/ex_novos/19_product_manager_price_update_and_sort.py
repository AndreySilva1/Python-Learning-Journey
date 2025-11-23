# Exercise Description:

# This program manages a list of products, updates their prices, 
# and displays multiple sorted versions of the list.

# Here’s what it does:
# Creates a deep copy of the original products list
# So the original data stays untouched.

# Applies a 10% price increase to the copied list
# Each price is multiplied by 1.10 and rounded to two decimals.

# Sorts the products in two different ways:
# By name, in descending order
# By price, in ascending order

# Displays all lists:
# Original products
# Updated products with price increase
# Products sorted by name
# Products sorted by price

import copy

products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]

# Copy for applying the 10% increase
updated_products = copy.deepcopy(products)

for product in updated_products:
    increased_price = product['price'] * 1.10
    product['price'] = round(increased_price, 2)


def display(items):
    for item in items:
        print(item)
    print()


# Sorted by name (descending)
products_sorted_by_name = sorted(
    copy.deepcopy(products),
    key=lambda item: item['name'],
    reverse=True
)

# Sorted by price (ascending)
products_sorted_by_price = sorted(
    copy.deepcopy(products),
    key=lambda item: item['price']
)

display(products)
display(updated_products)
display(products_sorted_by_name)
display(products_sorted_by_price)
