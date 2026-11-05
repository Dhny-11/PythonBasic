distance_mi = 10
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = True


if not distance_mi :
    print(False)

elif distance_mi <= 1:
    if not is_raining: 
        print(True)
    else : 
        print(False)
    
elif distance_mi <= 6: 
    if has_bike and not is_raining: 
        print(True)
    else : 
        print(False)

elif distance_mi > 6 : 
    if has_car or has_ride_share_app:
        print(True)
    else :
        print(False)


available_eggs = 1
available_flour = 2
available_sugar = 3

def check_kitchen_stock():
    total_items = available_eggs + available_flour + available_sugar
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')

check_kitchen_stock()

def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return available_eggs

    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use

use_eggs(available_eggs, 1)
print(available_eggs)

def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1

    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print('Made a fried egg. Yummy!')
    else:
        print('Could not make a fried egg. Not enough eggs!')

    return available_eggs
