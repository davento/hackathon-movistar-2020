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

@app.route('/request_codes')
def request_codes():
    return render_template('request_codes.html')

@app.route('/button', methods=['POST'])
def button():
    if(request.form['button1'] == 'Home'):
        return redirect(url_for('index'))
    else:
        return redirect(url_for('request_codes'))

#@app.route('/codes', method=['POST'])
#def codes():
#    return 



if __name__ == '__main__':
    app.run(debug=True, port=5000)