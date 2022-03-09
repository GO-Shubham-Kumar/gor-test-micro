import threading
from flask import Flask, jsonify, render_template, request
from flask_restful import Resource, Api
import asyncio
from flask_socketio import SocketIO, send
from datetime import datetime
import os
import pytz
import pymongo 
import urllib
from handle_users import register_user, login

tz_NY = pytz.timezone('Asia/Kolkata')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
api = Api(app)
socketio = SocketIO(app, cors_allowed_origins='*')

mongodb = pymongo.MongoClient("mongodb+srv://GO_Shubham_Kumar_Product_Architect:"+urllib.parse.quote_plus("Grey@2022")+"@cluster0.qyhhq.mongodb.net/Users?retryWrites=true&w=majority")

@app.route("/", methods=['GET', "POST"])
@app.route("/sync", methods=['GET'])
def index():
    now = datetime.now(tz_NY).strftime("%H:%M:%S")
    return {"data":"Sync Request Worked!", "time":now}

@app.route("/greetings", methods=['GET'])
def greet():

    greet_word = request.args.get('greet_word', default='Hello', type=str)
    name = request.args.get('name', default='', type=str)

    now = datetime.now(tz_NY).strftime("%H:%M:%S")
    print("INFO:::", datetime.now(tz_NY).strftime("%H:%M:%S") , f"{greet_word} {name}")

    if name == "nword":
        return {"error": "Internal Server Error"}, 500

    return {"data":f"{greet_word} {name}", "time":now}

@app.route("/greetings_post", methods=['POST'])
def greet_post():

    greet_word = request.json['greet_word']
    name = request.json['name']

    now = datetime.now(tz_NY).strftime("%H:%M:%S")
    print("INFO:::", datetime.now(tz_NY).strftime("%H:%M:%S") , f"{greet_word} {name}")

    if name == "nword":
        return {"error": "Internal Server Error"}, 500

    return {"data":f"{greet_word} {name}", "time":now}

@app.route("/async", methods=["GET"])
def async_req():
    receiving_time = datetime.now(tz_NY).strftime("%H:%M:%S")
    delta = request.args.get('delta', default=5, type=int)
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(hello(delta))

    sending_time = datetime.now(tz_NY).strftime("%H:%M:%S")

    return jsonify({
        "data": result, 
        "receiving_time":receiving_time, 
        "sending_time": sending_time
        }), 200

async def hello(wait_time=5):
    await asyncio.sleep(wait_time)
    return "Async Request Worked!"

@app.route("/register-get", methods=["GET"])
def handle_register_get():
    user_id = request.args.get('user_id', default='', type=str)
    age = request.args.get('age', default=0, type=int)
    password = request.args.get('password', default='', type=str)

    if "nword" in user_id:
        return {"error": "Internal Server Error"}, 500

    reg_flag = register_user(user_id, age, password) == 201
    if reg_flag == 201:
        return jsonify({"data":"User Registered"}), 201
    elif reg_flag == 409:
        return jsonify({"data":"User ID already exists"}), 409

@app.route("/register", methods=["POST"])
def handle_register():
    user_id = request.form.get('user_id', default='', type=str)
    age = request.form.get('age', default=0, type=int)
    password = request.form.get('password', default='', type=str)

    if "nword" in user_id:
        return {"error": "Internal Server Error"}, 500

    reg_flag = register_user(user_id, age, password) == 201
    if reg_flag == 201:
        return jsonify({"data":"User Registered"}), 201
    elif reg_flag == 409:
        return jsonify({"data":"User ID already exists"}), 409

@app.route(rule="/login", methods=["POST"])
def handle_login():
    user_id = request.form.get ('user_id', default='', type=str)
    password = request.form.get('password', default='', type=str)
    if login(user_id, password):
        return jsonify({"data":"Logged In"}), 200
    else:
        return jsonify({"data":"Invalid Credentials"}), 400

@app.route(rule="/circuit", methods=["GET"])
def handle_circuit():
    flag = request.args.get ('number', default=0, type=int)
    if flag > 0:
        return jsonify({"error":"Internal Server Error"}), 500
    else:
        return jsonify({"data":"Good to go."}), 200

if __name__ == "__main__":
    HOST = os.environ.get('SERVER_HOST', '127.0.0.1')
    PORT = int(os.environ.get('PORT', 5000))
    print(f"Running on port {PORT}")
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now(tz_NY).strftime('%Y-%m-%d %H:%M:%S')}: Running on {HOST}:{PORT}\n")
    app.run(host=HOST, port=PORT, debug=True)