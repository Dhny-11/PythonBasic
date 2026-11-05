full_dot = '●'
empty_dot = '○'

def create_character (character_name,STR,INT,CHA) :

    if not isinstance(character_name, str) :
        return 'The character name should be a string'
    if not character_name :
        return 'The character should have a name'
    if len(character_name) > 10:
        return 'The character name is too long'
    if  ' ' in character_name :
        return 'The character name should not contain spaces'
            

    if type(STR) is not int or type(INT) is not int or type(CHA) is not int:
        return 'All stats should be integers'
            
    if STR < 1 or INT < 1 or CHA < 1  :
        return 'All stats should be no less than 1'
    if STR > 4 or INT > 4 or CHA > 4  :
        return 'All stats should be no more than 4'
    if STR + INT + CHA != 7 :
        return 'The character should start with 7 points'

    str_bar = full_dot * STR + empty_dot * (10 - STR)
    int_bar = full_dot * INT + empty_dot * (10 - INT)
    cha_bar = full_dot * CHA + empty_dot * (10 - CHA)


    return f"{character_name}\nSTR {str_bar}\nINT {int_bar}\nCHA {cha_bar}"



character_name = create_character('ren', 4, 2, 1)
print(character_name)

