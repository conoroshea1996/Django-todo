from django.apps import apps
from django.test import TestCase
from .apps import TodoConfig


class TestToDoConfig(TestCase):
    def test_app(self):
        self.assertEqual('todo', TodoConfig.name)
        self.assertEqual('Todo', apps.get_app_config('todo').verbose_name)
