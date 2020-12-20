from flask import Flask, jsonify
from .db import collection
app = Flask(__name__)


@app.route("/rooms", methods=["GET"])
def index():
    data = collection.find({})
    newData = []
    for d in data:
            newData.append({**d, "_id": str(d["_id"]) })
    return jsonify(newData)
