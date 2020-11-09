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


@app.route('/button', methods=['POST'])
def button():
    return redirect(url_for('index'))


@app.route('/request_codes', methods=['POST'])
def codes():
    codigo = request.form['codigo']
    print(codigo)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)