from django.urls import path
from .views import TaskList, TaskDetail, UserDetail, Login

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('login/', Login.as_view()),
]
