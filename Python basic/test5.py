import math as m 
import module_name as module_alias 



m.sqrt(36)

from module_name import name1, name2 

from math import radians , sin , cos 
from module_name import * 


angle_degrees = 45 
angle_radius = radians(angle_degrees)

sine_value = sin(angle_radius)
cos_value = cos(angle_radius)

print(f"Sine of {angle_degrees} degrees is: {sine_value}")
print(f"Cosine of {angle_degrees} degrees is: {cos_value}")
print(f"Radus of {angle_degrees} degrees is: {angle_radius}")




pizza = {
    'name': 'Margherita',
    'price': 10.99,
    'calories': 250,
    'toppings': ['cheese', 'tomato sauce', 'basil']
    }

print(pizza['toppings'])

#mengganti valuse dari key 'toppings' dengan list baru
pizza['toppings'] = ['ketchup' , 'mustard' , 'mayonnaise']
print(pizza['toppings'])