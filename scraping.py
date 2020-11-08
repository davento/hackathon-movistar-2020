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

PATH = "./chromedriver"
userName="HACKATON10"
userPass="Hackaton_10"

searchCode = "12509324"


#abre el navegador
driver =webdriver.Chrome(PATH)
driver.implicitly_wait(10)

#ingresa a la web
driver.get("https://login.etadirect.com/telefonica-pe.etadirect.com/mobility/")
print(driver.title)

#ingresa las credenciales
nameField= driver.find_element_by_id("username")
nameField.send_keys(userName)
enterPassword(userPass)

#marcar el checkbox de sesion previa
closePreviusSessionCheckbox = driver.find_element_by_css_selector("span.checkbox-mark")
if closePreviusSessionCheckbox:
    print("Se encontro el checkbox")
time.sleep(1)
closePreviusSessionCheckbox.click()
time.sleep(1)
enterPassword(userPass)

#en este punto ya se está en la siguiente pagina 
#ironicamente buscar el boton de busqueda
buttonsPanel = driver.find_element_by_css_selector("*.buttons-panel")
searchButton = buttonsPanel.find_element_by_css_selector("*")
#for button in buttons:
searchButton.click()

#seleccionar barra de busqueda
searchBar= driver.find_element_by_css_selector("div.search-bar-input-hint-text")
searchBar.click()
searchBar = driver.find_element_by_css_selector("input.search-bar-input")
searchBar.send_keys(searchCode)
searchBar.send_keys(Keys.RETURN)
#print(searchBar)

#seleccionar la opcion no atendida
formLink = driver.find_element_by_css_selector("div.activity-title")
formLink.click()


input("press enter to finish")
driver.quit()
