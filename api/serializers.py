from rest_framework import serializers
from .models import Task
from datetime import datetime


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"

        