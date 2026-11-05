


products = {
    'Laptop': 1000,
    'Smartphone': 500,
    'Tablet': 300,
    'Headphones': 100,
}

for price in products.values():
    print(price)
    

for product in products.keys():
    print(product)
    

for product in products.items():
    print(product)
    
for product in enumerate(products):
    print(product)
    

my_set = {1, 2, 3, 4, 5}

print(my_set)

my_set.discard(4)
print(my_set)



