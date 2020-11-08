from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def enterPassword(pwrd):
    passField= driver.find_element_by_id("password")
    passField.send_keys(pwrd)
    passField.send_keys(Keys.RETURN)


#ingresa las credenciales
def enterName(usrNm):
    nameField= driver.find_element_by_id("username")
    nameField.send_keys(usrNm)

#marcar el checkbox de sesion previa
def clickCheckboxAndEnter(usrpss):
    closePreviusSessionCheckbox = driver.find_element_by_css_selector("span.checkbox-mark")
    if closePreviusSessionCheckbox:
        print("Se encontro el checkbox")
    time.sleep(0.5)
    closePreviusSessionCheckbox.click()
    time.sleep(0.5)
    enterPassword(usrpss)

#en este punto ya se está en la siguiente pagina 
#ironicamente buscar el boton de busqueda
def clickLupa():
    buttonsPanel = driver.find_element_by_css_selector("*.buttons-panel")
    searchButton = buttonsPanel.find_element_by_css_selector("*")
#for button in buttons:
    searchButton.click()

#seleccionar barra de busqueda
def searchSearchBox():
    searchBar= driver.find_element_by_css_selector("div.search-bar-input-hint-text")
    searchBar.click()
def searchElement(srchCd):
    searchBar = driver.find_element_by_css_selector("input.search-bar-input")
    searchBar.send_keys(srchCd)
    searchBar.send_keys(Keys.RETURN)
#print(searchBar)

def clickClearSearch():
    clearButton = driver.find_element_by_css_selector("div.search-bar-input-clear")
    clearButton.click()

#seleccionar la opcion no atendida
def clickBlueOption():
    formLink = driver.find_element_by_css_selector("div.activity-title")
    formLink.click()

#Ya estando en el formulario
#buscamos la informacion necesaria {nombre,descripcion,foto casa,foto cintillo}
#nombre y descripcion
def getTexts(result):
    clientName = driver.find_element_by_xpath("//*[text()='Cierre']/../../div[@class='cl-column']/div[21]/*[2]/*[1]/*[1]/*[text()]")
    description = driver.find_element_by_xpath("//*[text()='Cierre']/../../div[@class='cl-column']/div[30]/*[2]/*[1]/*[1]/*[text()]")
    result["cliente"] = clientName.get_attribute("innerText")
    result["descripcion"] = description.get_attribute("innerText")

#imagenes
# def getImages(result):
#    images = driver.find_elements_by_css_selector("img.inline-image")
#    print(images)

def extractData(driver, nombreDeUsuario, contraseniaDeUsuario, codigosBusqueda):
    if len(codigosBusqueda)== 0:
        return

    iteration = {
            "codigo":"",
            "cliente":"",
            "descripcion":""
            }
    result= []

    enterName(nombreDeUsuario)
    enterPassword(contraseniaDeUsuario)
    clickCheckboxAndEnter(contraseniaDeUsuario)

# solo para el primer codigo
    iteration["codigo"]=codigosBusqueda[0]
    clickLupa()
    searchSearchBox()
    searchElement(codigosBusqueda[0])
    clickBlueOption()
    getTexts(iteration)
    print(iteration)
    result.append(iteration)
    driver.back()

# para los demas codigos 
    for i in range(1,len(codigosBusqueda)):
        iteration["codigo"]=codigosBusqueda[i]
        clickLupa()
        clickClearSearch()
        searchSearchBox()
        searchElement(codigosBusqueda[i])
        clickBlueOption()
        getTexts(iteration)
        print(iteration)
        result.append(iteration)
        driver.back()
    

    return result

PATH = "./chromedriver"
userName="HACKATON10"
userPass="Hackaton_10"

searchCode =[
            "12509324",
            "12522060",
            "12565234"
        ]
#abre el navegador
driver =webdriver.Chrome(PATH)
driver.implicitly_wait(10)
#ingresa a la web
driver.get("https://login.etadirect.com/telefonica-pe.etadirect.com/mobility/")
print(driver.title)

extractData(driver,userName,userPass,searchCode)

input("press enter to finish")
driver.quit()
