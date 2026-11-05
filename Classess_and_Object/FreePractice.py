class test1:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name_Upper(self):
        self.name = self.name.upper()
        

    def display(self):
        print(f"Name: {self.name.title()}\nAge: {self.age}")
    

test1_instance = test1("Alice", 30)
#print(test1_instance.name)
#print(test1_instance.age)

test1_instance.display()


print("\n")

class Dog:
    species = "Canis lupus familiaris"  # Class attribute
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name.title()}\nAge: {self.age}\nSpecies: {self.species}")
        
    def bark(self):
        print(f"{self.name.title()} is barking!")

dog_instance = Dog("Alex", 5)
dog_instance.display()
dog_instance.bark()

print("\n")


class car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Make: {self.make.title()}\nModel: {self.model.title()}\nYear: {self.year}")


car1 = car("Toyota", "Camry", 2020)
car2 = car("Honda", "Civic", 2019)

car1.display()

print("\n")


class book:
    
    def __init__(self, title, author, year , pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def display(self):
        print(f"Title: {self.title.title()}\nAuthor: {self.author.title()}\nYear: {self.year}")
        
    def __len__(self):
        return len(self.title)
    
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"
    def __eq__(self, other):
        if isinstance(other, book):
            return self.pages == other.pages
        
        
book1 = book("The Great Gatsby", "F. Scott Fitzgerald", 1925 , 220)
book2 = book("To Kill a Mockingbird", "Harper Lee", 1960 , 220)

print(len(book1)) 
print(str(book1))  
print(book1 == book2)

print("\n")


class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
    print(item, end=' ' ) # Laptop Wireless mouse Ergo keyboard Monitor  
    
print("\n")
print(len(cart)) # 4
print(cart[3]) # Monitor

print('Monitor' in cart) # True
print('banana' in cart) # False

cart.remove('Ergo keyboard')

print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana') # banana is not in cart



class persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
person = persons("John", 30)

attr_name = input("Enter the attribute name to retrieve : ")
print(getattr(person, attr_name, "Attribute not found"))

print(getattr(person, 'name'))  
print(getattr(person, 'age'))
print(getattr(person, 'city' , 'Milano'))

print("\n")


for attr in dir(person):
    if not attr.startswith('__') and not callable(getattr(person, attr)):
        value = getattr(person, attr)
        print(f"{attr}: {getattr(person, attr)}")
    
print("\n")

class Configuration:
    pass

# Data loaded at runtime (like from a config or env file)
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Dynamically set attributes using dictionary keys and values
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url) # https://api.example.com
print(config_obj.timeout_sec) # 30
print(config_obj.max_retries) # 5
print(settings_data.items())


print("\n")


class Product:
    def __init__(self, name, price , ):
        self.name = name
        self.price = price

product_a = Product('T-Shirt', 25 , )

required_attributes = ['name', 'price', 'inventory_id']

for attr in required_attributes:
    if not hasattr(product_a, attr):
        print(f"ERROR: Product is missing the required attribute: '{attr}'")
    else:
        print(f'{attr}: {getattr(product_a, attr)}')
        
print("\n")

class UserSesion:
    def __init__(self, user_id, session_token):
        self.user_id = user_id
        self.sesion_token = session_token
        self.tempt_counter = 0
        

session = UserSesion('user123', 'abc123token')

attrubute_to_clean = ['auth_token', 'temp_counter']

for attr in attrubute_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f'Removed attribute: {attr}')
    
print('\nFinal attributes of session object:')

for attr in dir(session):
    if not attr.startswith('__') and not callable(getattr(session, attr)):
        print(f"{attr}: {getattr(session, attr)}")