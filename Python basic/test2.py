def apply_discount(price, discount) :


    if isinstance(price, (int, float)) :
        return('The price should be a number')
        if price <= 0 :
            print('The price should be greater than 0')
        else :
            print(False)
    
    if not discount  : 
        print('The discount should be a number')
        if discount < 0 and discount > 100 : 
            print('The discound shoudl be between 0 and 100')
        else :
            print(False)



apply_discount('a','2')