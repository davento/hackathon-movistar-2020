
import re

def validate(dictionary):
    nombres = dictionary["cliente"]
    contacto = dictionary["descripcion"]
    
    check_si_es_palabra = not (bool(re.search(r'\d', nombres)))
    numero_de_palabras = nombres.split(" ")
    check_si_es_numero = str.isdecimal(contacto)

    if(check_si_es_numero and check_si_es_palabra and (len(contacto)== 9 or len(contacto)==7) and len(numero_de_palabras)>=2):
        return True
    else:
        return False

dict = {
    "cliente": "Juan Pablo",
    "descripcion": "955505868"
}

print(validate(dict))