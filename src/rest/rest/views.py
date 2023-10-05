from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
from pymongo import MongoClient
from rest_framework import status, serializers
from bson import ObjectId

mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db = MongoClient(mongo_uri)['test_db']

class TodoItemSerializer(serializers.Serializer):
    _id = serializers.CharField(required=False)
    text = serializers.CharField()

todo_collection = db.todo_list

class TodoListView(APIView):

    def get(self, request):
        # Implement this method - return all todo items from db instance above.
        todos = list(todo_collection.find())
        serializer = TodoItemSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        # Implement this method - accept a todo item in a mongo collection, persist it using db instance above.
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            todo_item = serializer.validated_data
            todo_collection.insert_one(todo_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        # Implement this method - accept a todo item in a mongo collection, persist it using db instance above.
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            todo_item = serializer.validated_data
            todo_id = todo_item.get("_id")

            if todo_id:
                todo_id = ObjectId(todo_id)
            else:
                return Response({"error": "request needs to have an _id field"}, status=status.HTTP_400_BAD_REQUEST)

            result = todo_collection.update_one({"_id": todo_id}, {"$set": {"text": todo_item.get("text")}})
            if result.matched_count == 1:
                return Response(todo_item, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid id (Item does not exist)"}, status=status.HTTP_400_BAD_REQUEST )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        # Implement this method - accept a todo item in a mongo collection, persist it using db instance above.
        data = request.data
        _id = data["_id"]
        if not _id:
            return Response({"error": "request needs to have an _id field"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            _id = ObjectId(_id)
            result = todo_collection.delete_one({"_id": _id})
            if result.deleted_count == 1:
                return Response({}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "Invalid id (Item does not exist)"}, status=status.HTTP_400_BAD_REQUEST )
        except:
            return Response({"error": "Failed to delete todo"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

