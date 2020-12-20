from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("MONGO_URI"))
db = client.Hotel
collection = db.rooms
