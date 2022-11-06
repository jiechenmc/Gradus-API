from bson import json_util
from pymongo import MongoClient
from app.core.model import Record


def parse_json(data):
    return json_util.loads(json_util.dumps(data))


def find(collection: MongoClient, field: str, q: str) -> list[Record]:
    return parse_json(
        collection.find({field: {
            "$regex": q,
            "$options": "i"
        }}, {"_id": False}))