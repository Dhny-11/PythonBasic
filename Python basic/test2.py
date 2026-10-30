


#apply_discount('a','2')

def create_character (character_name ) :
    if not isinstance(character_name, str) :
        return 'The character name should be a string'
    if not character_name :
        return 'The caracter should have a name'
    if len(character_name) > 10:
        return 'The character name is too long'
    if ' ' in character_name:
        return 'The caracter name should not contain spaces'
        
        
    return character_name






character_name = create_character('')
print(character_name)

numbers = [1,2,3,4,5]
numbers.insert(3 , 3.4)

add_number = ['Hello',123,144,'World']

numbers.extend(add_number)

print(numbers)

print(numbers.index('Hello'))

dev ='Djoko'

print(tuple(dev))

dev_name = ('Djoko' , 25 , 'Front-End')
name , age , job = dev_name 

namae , *sisa = dev_name 

print(namae)
print(sisa)

print(name )
print(age)
print(job)


for num in range(1,5):
    print(num)
    
programming_language = ('C++, PHP, Python , Java ,JavaScript')
print(sorted(programming_language , key=len))


nom = list(range(2 , 100 , 2))
print(nom)


language = ['Spanish' , 'Japan' , 'Netherland' , 'Russian']

index = 0

for language in language :
    print(f"Index {index} and language {language}")
    index += 1
    

list(enumerate(language))

print(language) 


languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages ,1):
    print(f'Index {index} and language {language}')
    

devs = ['Djoko' , 'Samsudin' , 'Eva' , 'Susan']



for name , lang in zip(devs, languages):
    print(f'name : {name}')
    print(f'language : {lang}')
    
    

even_number = []

for num in range (21):
    if num % 2 == 0:
        even_number.append(num)

print(even_number)


even_numbers = [num for num in range(31) if num % 2 == 0]
print (even_numbers)

angka = [num for num in range(101)]
result = [(num , 'Even') if num % 2 == 0 else (num,'Odd') for num in angka]

print(result)



word = [ 'tree' , 'sky' , 'mountain' , 'river' , 'cloud' , 'sun']

def is_long_word(word):
    return len(word) > 4

def is_short_word(word):
    return len(word) < 5 

long_word = list(filter(is_long_word, word))
print(long_word)

short_word = list(filter(is_short_word, word))
print(short_word)


celcius =[ 0 , 10, 20 ,30, 40, 50]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32 

fahrenheit = list(map(to_fahrenheit , celcius))
print(fahrenheit)