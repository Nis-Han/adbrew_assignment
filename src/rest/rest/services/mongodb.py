import os
from pymongo import MongoClient
from bson import ObjectId

mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db = MongoClient(mongo_uri)['test_db']

class TodoDB:

    def __init__(self):
        self.todo_collection = db.todo_list

    def get_all_todo_items(self):
        try: 
            todos = list(self.todo_collection.find())
            return {"data": todos, "status": 200}
        except Exception as e:
            return {"data": {"error": "Problem connecting with the DB"}, "status": 500}
        
    def insert_todo_item(self, data):
        try:
            result = self.todo_collection.insert_one(data)
            return {"data": data, "status": 201}
        except Exception as e:
            return {"data": {"error": str(e)}, "status": 400}

    def update_todo_item(self, data):
        todo_id = data.get("_id")
        if not todo_id:
            return {"data": {"error": "request needs to have an _id field"}, "status": 400}

        try:
            todo_id = ObjectId(todo_id)
        except Exception as e:
            return {"data": {"error": "Invalid id (Item does not exist)"}, "status": 400}

        result = self.todo_collection.update_one({"_id": todo_id}, {"$set": {"text": data.get("text")}})
        if result.matched_count == 1:
            return {"data": data, "status": 200}
        else:
            return {"data": {"error": "Invalid id (Item does not exist)"}, "status": 400}

    def delete_todo_item(self, data):
        _id = data.get("_id")
        if not _id:
            return {"data": {"error": "request needs to have an _id field"}, "status": 400}
        
        try:
            _id = ObjectId(_id)
        except Exception as e:
            return {"data": {"error": "Invalid id (Item does not exist)"}, "status": 400}

        result = self.todo_collection.delete_one({"_id": _id})
        if result.deleted_count == 1:
            return {"data": {}, "status": 204}
        else:
            return {"data": {"error": "Invalid id (Item does not exist)"}, "status": 400}
