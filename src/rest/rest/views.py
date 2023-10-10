from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.client_services import TodoListService
from .utils.serializers import TodoItemSerializer
import json

class TodoListView(APIView):

    def get(self, request):
        service = TodoListService()
        todos = service.get_todo_items()
        return Response(todos, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            service = TodoListService()
            result = service.create_todo_item(data)
            return Response(result["data"], status=result["status"])
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            service = TodoListService()
            result = service.update_todo_item(serializer.validated_data)
            return Response(result["data"], status=result["status"])
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            service = TodoListService()
            result = service.delete_todo_item(serializer.validated_data)
            return Response(result["data"], status=result["status"])
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
