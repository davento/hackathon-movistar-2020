from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'movistarHackaton'

def check_for_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'missign token'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Invalid token'}), 403
        return func(*args, **kwargs)
    return wrapped

@app.route('/public')
def public():
    return 'Anyone can see this'

@app.route('/auth')
@check_for_token
def public():
    return 'This is only viewable with token'

@app.route('/login')
def login():
    
    return 

if __name__ == '__main__':
    app.run()
