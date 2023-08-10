from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.forms.models import model_to_dict
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication


from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, UserSerializer


class TaskList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        user = request.user

        tasks = user.tasks
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, reqeust: Request):
        data = reqeust.data

        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class TaskDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk: int) -> Response:
        try:
            user = request.user

            task = user.tasks.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response(
                data={'error': 'task does not exist.'},
                status=status.HTTP_404_NOT_FOUND)


    def put(self, request: Request, pk: int):
        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class UserDetail(APIView):
    def get(self, reqeust: Request, pk: int) -> Response:
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(user)

        return Response(serializer.data)


class Login(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        user = request.user

        token = Token.objects.create(user=user)

        return Response({'token': token.key})