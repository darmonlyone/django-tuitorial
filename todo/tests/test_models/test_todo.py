from django.test import TestCase
from todo.models import Todo


class TestTodo(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.darm = "darm"
        names = ["Do jame", "Swimming", "Tang Pool", "Say hi", "DO homework"]
        for i in names:
            a = Todo(name=i, is_done=False)
            a.save()

    def setUp(self):
        pass

    def test_init(self):
        self.darm
        b = Todo.objects.get(name="Do jame")
        self.assertIsNotNone(b)
        self.assertFalse(b.is_done)
        b.set_done()
        self.assertTrue(b.is_done)

    def test_change_name(self):
        b = Todo.objects.get(name="Swimming")
        b.name = "Jame"
        b.save()
        c = Todo.objects.filter(name="Swimming")
        d = Todo.objects.get(name__exact="Jame")
        self.assertEquals(len(c), 0)
        self.assertIsNotNone(d)

    @classmethod
    def tearDownClass(cls):
        b = Todo.objects.all()
        b.delete()
