from flask import Flask, jsonify
from .db import collection
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)


@app.route("/rooms", methods=["GET"])
def index():
    data = collection.find({})
    newData = []
    for d in data:
            newData.append({**d, "_id": str(d["_id"]) })
    return jsonify({"rooms": newData})
