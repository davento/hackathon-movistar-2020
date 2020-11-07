from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "./chromedriver"
userName="HACKATON10"
userPass="Hackaton_10"


#abre el navegador
driver =webdriver.Chrome(PATH)

#ingresa a la web
driver.get("https://login.etadirect.com/telefonica-pe.etadirect.com/mobility/")
print(driver.title)

#ingresa las credenciales
nameField= driver.find_element_by_id("username")
nameField.send_keys(userName)

passField= driver.find_element_by_id("password")
passField.send_keys(userPass)
passField.send_keys(Keys.RETURN)

#marca la checkbox de error(aun no hecho xq me empezo a funcionar y F xD)

#en este punto ya se está en la siguiente pagina 
#ironicamente buscar el boton de busqueda
buttons= driver.find_elements_by_class_name("jbf-icon-button action-global-search-icon")
print(buttons)

for but in buttons:
    print(but)

#seleccionar barra de busqueda
searchBar= driver.find_elements_by_class_name("search-bar-input")


#driver.quit()
