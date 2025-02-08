from .serializers import TaskSerializer, TaskCreateSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .permissions import IsAuthor
from .models import Task
from django.utils import timezone


class TaskList(ListAPIView):
    permission_classes = (IsAuthor, )
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreate(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TaskDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthor, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


from django.views.generic import TemplateView
from .models import Task

class TaskListView(TemplateView):
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context






