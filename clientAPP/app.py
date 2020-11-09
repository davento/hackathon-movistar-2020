from flask import *
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/request_codes', methods=['POST'])
def codes():
    APIaddress = 'http://127.0.0.1:5000/v1/validate?'
    try:
        codigo = request.get_json()['codigo']
        print(codigo)
        #integrar con hAckPI
        ADDRESS= APIaddress + "code=" + codigo
        print(ADDRESS)
        resp =  requests.get(ADDRESS).json()
        print(resp)
    except Exception as e:
        print(e)

    finally:
        if(resp["Error"]=="All ok" and resp["status"]):
            respuesta = 'El formulario numero '+ codigo + ' es conforme'
        else:
            respuesta ='El formulario numero '+ codigo + 'no es conforme'

        respuesta += "|Nombre:\n\t" + resp["Name"] + "|Descripcion:\n\t" + resp["Description"]
        
        return jsonify({
            'respuesta': respuesta
        })


if __name__ == '__main__':
    app.run(debug=True, port=6969, host='127.0.0.1')
