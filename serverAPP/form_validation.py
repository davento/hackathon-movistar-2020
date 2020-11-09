
import re

def validate(name, description):
   
    check_if_word = not (bool(re.search(r'\d', name)))
    if (not check_if_word):
        return False
    
    number_of_words = name.split(" ")
    if (len(number_of_words) < 2):
        return False

    for number in re.findall(r"\d+", description):
        if(not (str.isdecimal(number) and (len(number)== 9 or len(number)==7))):
            return False
    
    return True