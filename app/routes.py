from app import app, db
from flask import request, jsonify
from flask_login import current_user, login_user, logout_user
from app.models import User
import http.client

@app.route('/')
@app.route('/index')
def index():
    print("pooo!")
    return "Hello, World!"


@app.route('/login', methods=['POST'])
def login():
    # if current_user.is_authenticated:
    # TODO https://github.com/adekoder/flask-validator
    print(request.form)
    user = User.query.filter_by(username=request.form['username']).first()
    if user is None or not user.check_password(request.form['password']):
        response = jsonify({'message':'Invalid username or password'})
        return response, 401
    login_user(user)
    response = jsonify({'user': User.as_dict(user)})        
    return response, 200

@app.route('/logout')
def logout():
    logout_user()
    return 200

@app.route('/register', methods=['POST'])
def register():
    # if current_user.is_authenticated:

    # TODO https://github.com/adekoder/flask-validator
    user = User(username=request.form['username'], email=request.form['email'])
    user.set_password(request.form['password'])
    db.session.add(user)
    db.session.commit()
    response = jsonify({'user': User.as_dict(user)})        
    return response, 200

@app.route('/fetch', methods=['GET'])
def getShareData():

    conn = http.client.HTTPSConnection("stock-data-yahoo-finance-alternative.p.rapidapi.com")

    headers = {
    'x-rapidapi-host': app.config['RAPIDAPI_HOST'],
    'x-rapidapi-key': app.config['RAPIDAPI_KEY']
    }

    conn.request("GET", "/v6/finance/quote?symbols=PMGOLD.AX&region=AU", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))






