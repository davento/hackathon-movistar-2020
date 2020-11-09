from flask import *
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/request_codes', methods=['POST'])
def codes():
    APIaddress = "http://127.0.0.1:5000/v1/validate?"
    try:
        codigo = request.get_json()['codigo']
        #integrar con hAckPI
        ADDRESS= APIaddress + "code=" + codigo
        resp =  requests.get(ADDRESS).json()
        print(resp)
        resp = json.load(resp)
        print(resp)


        if(resp["Error"]=="All ok" and resp["status"]):
            respuesta = 'El formulario numero '+ codigo + ' es conforme'
        else:
            respuesta ='El formulario numero '+ codigo + 'no es conforme'
        
        return jsonify({
            'respuesta': respuesta
        })
    except Exception as e:
        print('Ocurrio un error')


if __name__ == '__main__':
    app.run(debug=True, port=6969, host='127.0.0.1')
