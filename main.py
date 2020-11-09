from scraping import *
from  form_validation import *
from recognition  import *

def main():
    PATH = "./chromedriver.exe"
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

    result = extractData(driver,userName,userPass,searchCode)

    for data in result:
        print(data["codigo"], "es: ")
        if validate(data["cliente"],data["descripcion"]):
            print("correcto")
        else:
            print("incorrecto")

    print("------------------imagenes--------------------")
    image_comformity()

    input("press enter to finish")
    driver.quit()

if __name__== '__main__':
    main()
