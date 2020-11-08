from scraping import *
from  form_validation import *

def main():
    PATH = "./chromedriver"
    userName="HACKATON10"
    userPass="Hackaton_10"

    searchCode =[
                "12509324",
                "12522060",
                "12565234"
            ]
#abre el navegador
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(10)
#ingresa a la web
    driver.get("https://login.etadirect.com/telefonica-pe.etadirect.com/mobility/")
    print(driver.title)

    resultado = extractData(driver,userName,userPass,searchCode)

    for datos in resultado:
        print(datos["codigo"], "es: ")
        if validate(datos["cliente"],datos["descripcion"]):
            print("correcto")
        else:
            print("incorrecto")


    input("press enter to finish")
    driver.quit()

if __name__== '__main__':
    main()
