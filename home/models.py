from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200,default="test")

    def __str__(self) -> str:
        return self.title