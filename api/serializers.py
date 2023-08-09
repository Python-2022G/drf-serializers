from rest_framework import serializers
from .models import Task
from datetime import datetime


class TaskCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(allow_null=True)
    completed = serializers.BooleanField(default=False)
    created = serializers.DateTimeField(default=datetime.now())


    def create(self, validated_data: dict):
        return Task.objects.create(
            title=validated_data.get('title'),
            description=validated_data.get('description'), 
            completed=validated_data.get('completed')
        )


class TaskRetrieveSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(allow_null=True)
    completed = serializers.BooleanField(default=False)
    created = serializers.DateTimeField(default=datetime.now())


    def to_representation(self, isntance: Task):
        return {
            "id": isntance.id,
            'title': isntance.title
        }


class TaskUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200, required=False)
    description = serializers.CharField(required=False)
    completed = serializers.BooleanField(required=False)


    def update(self, instace: Task, validated_data):
        instace.title = validated_data.get('title', instace.title)
        instace.description = validated_data.get('description', instace.description)
        instace.completed = validated_data.get('completed', instace.completed)

        instace.save()

        return instace