#basic API with authentication
from flask import Flask, jsonify, request, make_response
import jwt

import datetime
from functools import wraps
app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretkey'
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}),403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is missing or invalid!'}),403
        return f(*args,**kwargs)

    return decorated

@app.route('/unprotected')
def unprotected():
    return jsonify({'message': 'Anyone can view this!'})

@app.route('/protected/<int:n>')
@token_required
def protected(n):
    return jsonify({'message' : 'This is only available for people with token ids.'})



@app.route('/login/')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({'user' : auth.username,'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    return make_response('Could not verify!', 401,{'WWW-Authenticate' :'Basic realm="Login Required"'})



@app.route("/")
def page_home():
    return render_template('table.html')


if __name__=="__main__":
    app.run(debug=True)