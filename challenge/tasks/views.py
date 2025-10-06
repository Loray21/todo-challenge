from rest_framework import viewsets, permissions, filters
from .models import Task
from .serializers import TaskSerializer
from django.utils.dateparse import parse_date
import logging

logger = logging.getLogger(__name__)  # logger simple


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        logger.info(f"Tarea creada: {task.title} por usuario {self.request.user.username}")

    def get_queryset(self):
        # Only show the authenticated user's tasks
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        # 🔹 Filtrar por fecha exacta (YYYY-MM-DD)
        date_str = self.request.query_params.get('created_at')
        if date_str:
            date_obj = parse_date(date_str)
            if date_obj:
                queryset = queryset.filter(created_at__date=date_obj)

        return queryset
