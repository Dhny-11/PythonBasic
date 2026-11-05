#def number_pattern (n):
#    for num in range(n):
#        print (num, end=" ")
    
    
#number_pattern(3)
import random



numbers = [1,2,3,4,5]
print(len(numbers))



Cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
print(list(Cities[2]))

city , state ,*rest = Cities
print(city)
print(state) 


random_numbers = [1, 2, 3, 4, 5]
for num in random_numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

sec_num = random.randint(1, 50) 
guest_num = 0 

while guest_num != sec_num:
    guest_num = int(input("Enter a number: "))
    if guest_num < sec_num:
        print("Too low")
    elif guest_num > sec_num:
        print("Too high")
    else:
        print("You guessed it!")