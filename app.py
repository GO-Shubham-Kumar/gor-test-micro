import threading
from flask import Flask, jsonify, render_template, request
from flask_restful import Resource, Api
import asyncio
from flask_socketio import SocketIO, send
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
api = Api(app)
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route("/", methods=['GET', "POST"])
@app.route("/sync", methods=['GET'])
def index():
    now = datetime.now().strftime("%H:%M:%S")
    return {"data":"Sync Request Worked!", "time":now}


@app.route("/async", methods=["GET"])
def async_req():
    receiving_time = datetime.now().strftime("%H:%M:%S")
    delta = request.args.get('delta', default=5, type=int)
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(hello(delta))

    sending_time = datetime.now().strftime("%H:%M:%S")

    return jsonify({
        "data": result, 
        "receiving_time":receiving_time, 
        "sending_time": sending_time
        }), 200

async def hello(wait_time=5):
    await asyncio.sleep(wait_time)
    return "Async Request Worked!"


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send(message, broadcast=True)

@app.route("/websocket", methods=["GET", "POST"])
def websocket():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)