from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    # Cualquier cliente puede hacer solicitudes
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
