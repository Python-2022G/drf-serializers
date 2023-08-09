from django.urls import path
from .views import TaskList, TaskDetail, UserDetail

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
