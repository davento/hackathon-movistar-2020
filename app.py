from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/request_codes', methods=['POST'])
def codes():
    try:
        codigo = request.get_json()['codigo']

        if(True):
            respuesta = 'El formulario numero '+ codigo + ' es conforme'
        else:
            respuesta ='El formulario numero '+ codigo + 'no es conforme'
        
        return jsonify({
            'respuesta': respuesta
        })
    except Exception as e:
        print('Ocurrio un error')
    


if __name__ == '__main__':
    app.run(debug=True, port=5000)