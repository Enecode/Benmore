from django.urls import path, include
from . import views

urlpatterns = [
    path('project-create/', views.ProjectCreateView.as_view(), name='project-create'),
    path('projects/', views.ProjectListCreateView.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('task-create/', views.TaskCreateView.as_view(), name='task-create'),
    path('projects/<int:project_pk>/tasks/', views.TaskListCreateView.as_view(), name='task-list'),
    path('projects/<int:project_pk>/tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('filtered-projects/', views.FilteredProjectList.as_view(), name='filtered-project-list'),
]