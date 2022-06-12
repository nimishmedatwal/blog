from django.db import models

class blog(models.Model):
    title=models.CharField(max_length=100)
    content = models.CharField(max_length=2550)

    def __str__(self):
        return self.taskn