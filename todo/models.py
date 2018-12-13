from django.db import models


# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=50)
    is_done = models.BooleanField(default=False)

    def set_done(self):
        if not self.is_done:
            self.is_done = True

    # toString
    def __str__(self):
        if self.is_done:
            return self.name + " is done"
        else:
            return self.name + " is not done"
