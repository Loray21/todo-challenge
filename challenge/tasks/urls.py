# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Crear un router y registrar el ViewSet
routerTasks = DefaultRouter()
routerTasks.register(r'tasks', TaskViewSet, basename='task')


# Las rutas se generarán automáticamente
urlpatterns = [
    path('', include(routerTasks.urls)),  # Incluye las rutas generadas por el router
]