from .mongodb import TodoDB

class TodoListService:

    def __init__(self):
        self.db = TodoDB()

    def get_todo_items(self):
        result = self.db.get_all_todo_items()
        if result["status"] ==200:
            todos = result["data"]
            formatted_todos = [
                {"_id": str(todo["_id"]), "text": todo["text"]} for todo in todos
            ]
            return formatted_todos
        else:
            return result
        
    def create_todo_item(self, data):
        result = self.db.insert_todo_item(data)
        if result["status"] == 201:
            return {"data": {"_id": str(result["data"]["_id"]), "text": result["data"]["text"]}, "status": 201}
        else:
            return result
    
    def update_todo_item(self, data):
        result = self.db.update_todo_item(data)
        if result["status"] == 200:
            return {"data": {"_id": str(data["_id"]), "text": data["text"]}, "status": 200}
        else:
            return result
    
    def delete_todo_item(self, data):
        result = self.db.delete_todo_item(data)
        return result
