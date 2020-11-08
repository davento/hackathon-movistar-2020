

def validate(dictionary):
    nombres = dictionary["cliente"]
    contacto = dictionary["descripcion"]

    numero_de_palabras = nombres.split(" ")

    check_si_es_numero = str.isdecimal(contacto)
    if(check_si_es_numero and (len(contacto)== 9 or len(contacto)==7) and len(numero_de_palabras)>=2):
        return True
    else:
        return False

dict = {
    "cliente": "Juan Pablo",
    "descripcion": "955505868"
}

print(validate(dict))