from rest_framework import viewsets
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.get('user_id')
        if user_id:
            serializer.save(user_id=user_id)
        else:
            serializer.save()

    def perform_update(self, serializer):
        user_id = self.request.data.get('user_id')
        if user_id:
            serializer.save(user_id=user_id)
        else:
            serializer.save()
