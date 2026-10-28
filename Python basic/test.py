mystr = 'hello world'
splitwrd = mystr.split()
print(splitwrd)

str1 = '    hello   world   '
stripwrd = str1.strip()
print(stripwrd)
print (str1)

str2 = 'hello world'
startwith = str2.startswith('hello')
print(startwith)

str3 = 'hello world'
capstr = str3.capitalize()
print(capstr)

titlestr = str3.title()
print(titlestr)   

te = 10 
te **=4

print (te)


distance_mi = 10
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = True

if distance_mi > 1 and distance_mi <= 6 :
    if  is_raining == True and has_bike == False : 
        print('False') 
    elif is_raining == False and has_bike == False:
        print('Ture')
    elif is_raining == False and has_bike == True: 
        print('False')
    elif is_raining == True and has_bike == True: 
        print('True')
else : 
    print('False')
    
if distance_mi > 6 and has_ride_share_app == True:
    print('True')
elif distance_mi > 6 and has_car == True :
    print ('True')

    