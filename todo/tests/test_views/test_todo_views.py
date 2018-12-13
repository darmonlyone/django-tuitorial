from django.test import TestCase
from django.urls import reverse

from todo.models import Todo


class TestTodoView(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.darm = "darm"
        names = ["Do jame", "Swimming", "Tang Pool", "Say hi", "DO homework"]
        for i in names:
            a = Todo(name=i, is_done=False)
            a.save()

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_list(self):
        response = self.client.get(reverse('list_todo'))
        self.assertIn(response, "")

    def test_set_some_done(self):
        a = Todo.objects.first()
        response = self.client.get(reverse('detail', args=[a.id]))
        self.assertIn(response, "Do jame is not done")


    @classmethod
    def tearDownClass(cls):
        b = Todo.objects.all()
        b.delete()
