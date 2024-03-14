
# Write your test here
import unittest
from django.test import TestCase
from Benmore_app.models import Project, Task
from Benmore_app.serializers import ProjectSerializer, TaskSerializer

class ProjectTestCase(TestCase):
    def setUp(self):
        self.project = Project.objects.create(name="Test Project", description="This is a test project", status="OPEN")
        Task.objects.create(name_of_task="Test Task", description="This is a test task", completed=False, project=self.project)

    def test_project_name(self):
        project = Project.objects.get(name="Test Project")
        self.assertEqual(project.name, "Test Project")

    def test_project_serializer(self):
        serializer = ProjectSerializer(self.project)
        self.assertEqual(serializer.data, {'id': 1, 'name': 'Test Project', 'description': 'This is a test project', 'status': 'OPEN', 'tasks': [{'id': 1, 'project': 1, 'project_name': 'Test Project', 'name_of_task': 'Test Task', 'description': 'This is a test task', 'completed': False}]})

class TaskTestCase(TestCase):
    def setUp(self):
        self.project = Project.objects.create(name="Test Project", description="This is a test project", status="OPEN")
        self.task = Task.objects.create(name_of_task="Test Task", description="This is a test task", completed=False, project=self.project)

    def test_task_name(self):
        task = Task.objects.get(name_of_task="Test Task")
        self.assertEqual(task.name_of_task, "Test Task")

    def test_task_serializer(self):
        serializer = TaskSerializer(self.task)
        self.assertEqual(serializer.data, {'id': 1, 'project': 1, 'project_name': 'Test Project', 'name_of_task': 'Test Task', 'description': 'This is a test task', 'completed': False})

if __name__ == '__main__':
    unittest.main()
