import threading
from flask import Flask, jsonify, render_template
from flask_restful import Resource, Api
import asyncio
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
api = Api(app)
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route("/", methods=['GET'])
@app.route("/sync", methods=['GET'])
def index():
    return {"data":"Sync Request Worked!"}


@app.route("/async", methods=["GET"])
def async_req():
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(hello())
    return jsonify({"result": result}), 200

async def hello():
    await asyncio.sleep(5)
    return "Async Request Worked!"


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send(message, broadcast=True)

@app.route("/websocket", methods=["GET"])
def websocket():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)