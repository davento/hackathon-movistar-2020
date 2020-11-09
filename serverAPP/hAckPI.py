import flask
from flask import request, jsonify
import heapq as pq
import time

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




#esto aun no se como hacerlo o como sera xD
#@app.route("/sendImage/<tipo>", methods=['POST'])
#@app.route("/sendImage/<tipo>", methods=['POST'])


