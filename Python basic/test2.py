


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