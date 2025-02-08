from django.urls import path
from .views import TaskDetail, TaskList, TaskCreate, TaskListView
urlpatterns = [
    path('task/', TaskList.as_view(), name='task_list'),
    path('task/create/', TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('t/', TaskListView.as_view(), name='t')

]