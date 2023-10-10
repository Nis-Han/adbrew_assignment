from rest_framework import serializers

class TodoItemSerializer(serializers.Serializer):
    _id = serializers.CharField(required=False)
    text = serializers.CharField(required=False)
