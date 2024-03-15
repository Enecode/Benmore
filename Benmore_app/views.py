from rest_framework import generics, filters
from rest_framework import serializers

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    "View for listing and creating projects"
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Check for unique project name before saving
        if Project.objects.filter(name=serializer.validated_data['name']).exists():
            raise serializers.ValidationError('Project with that name already exists.')
        serializer.save()

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    "View for retrieving, updating and deleting projects"
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TaskListCreateView(generics.ListCreateAPIView):
    "View for listing and creating tasks within a project"
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        "Check for unique task title within the same project before saving."
        project_id = self.kwargs.get('project_pk')
        if Task.objects.filter(project_id=project_id, title=serializer.validated_data['title']).exists():
            raise serializers.ValidationError('Task with that title already exists in this project.')
        serializer.save()

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    "View for retrieving, updating and deleting tasks within a project"
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FilteredProjectList(generics.ListAPIView):
    "View for listing projects with a specific status"
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    # Filter projects by name or description if search query is provided in the query parameters.
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(name__icontains=search_query) | queryset.filter(description__icontains=search_query)
        return queryset
    
    def get_queryset(self):
        "Filter projects by status if status is provided in the query parameters."
        queryset = super().get_queryset()
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer