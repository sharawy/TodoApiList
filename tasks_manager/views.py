from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from tasks_manager.models import TodoTask
from tasks_manager.serializers import TodoTaskSerializer
from rest_auth.views import LoginView

class TasksViewSet(viewsets.ModelViewSet):
    """
        Todo tasks endpoint
    """
    serializer_class = TodoTaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return TodoTask.objects.all()
        else:
            return TodoTask.objects.filter(owner=self.request.user)