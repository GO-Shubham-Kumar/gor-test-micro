import threading
from flask import Flask, jsonify
from flask_restful import Resource, Api
import asyncio

app = Flask(__name__)
api = Api(app)

@app.route("/", methods=['GET'])
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

if __name__ == "__main__":
    app.run(debug=True)