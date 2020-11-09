import flask
from flask import request, jsonify
import heapq as pq
import time
#hum 
from scraping import *
from  form_validation import *
from recognition  import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

codesToCheck = [] # (prioridad, orden de entrada, data)
codesChecked = {}

def getResponse(code):
    if code in codesChecked:
        return codesChecked.pop(code)
    else:
        time.sleep(0.5)
        return getResponse(code)
                                        #este es el request.args --v
@app.route("/v1/validate", methods=['GET'])#IP:port/v1/validate?code=<code>
def validateCode():
    if "code" in request.args:
        try:
            code = int(request.args["code"])#el codigo es un numero de 8 cifras
        except:
            return "Error: bad formated code"
    else:
        return "Error: no code provided"

    pq.heappush(codesToCheck, (1,len(codesToCheck),request.args["code"]))
    validation = getResponse(request.args["code"])

    return jsonify(validation)

def openConectionTOA(driver,name,passw):
    enterName(name,driver)
    enterPassword(passw,driver)
    try:
        clickCheckboxAndEnter(passw,driver)
    except:
        print("no check box detected")

def searchForUserData(driver,searchcode,clearBox):
        data={"Error":" All ok"}
        clickLupa(driver)
        if clearBox:
            clickClearSearch(driver)
        searchSearchBox(driver)
        searchElement(searchcode,driver)
        try:
            clickBlueOption(driver)
            getTexts(data,driver)#esto modifica a data
            driver.back()
        except:
            data= {"Error":"bad code format","Client":"","Description":""}

        return data.copy()#el copy es x siacaso no valla a ser q nos de un error :v

def launchScrapper():
    PATH = "./chromedriver"
    userName="HACKATON10"
    userPass="Hackaton_10"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.get("https://login.etadirect.com/telefonica-pe.etadirect.com/mobility/")
    control=0
    openConectionTOA(driver,userName,userPass)
    return (driver,control)#kiero q se pase este (por referencia) :v

def main():
#abre el navegador
    initial = launchScrapper()
    driver = initial[0]
    control = initial[1]

    app.run()
    while 1:
        while len(codesToCheck)>0:
            priorityCode = pq.heappop(codesToCheck)[2]
            codesChecked[priorityCode] = searchForUserData(driver,priorityCode,control)

            control=1#esto es para q se comporte algo diferente solo en la 1ra iteracion

        time.sleep(0.5)#espera a q se llene la cola


#esto aun no se como hacerlo o como sera xD
#@app.route("/sendImage/<tipo>", methods=['POST'])
#@app.route("/sendImage/<tipo>", methods=['POST'])

if __name__ == "__main__":
    main()

