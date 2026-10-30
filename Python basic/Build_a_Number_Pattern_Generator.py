def number_pattern(n) : 

    if not isinstance(n , int):
        return 'Argument must be an integer value.'
    if n < 1 : 
        return 'Argument must be an integer greater than 0.'

    hasil = []

    for num in range(1 , n + 1):
        hasil.append(str(num))
    
    return " ".join(hasil)
print(number_pattern(4))   
