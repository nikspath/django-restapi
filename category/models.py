from django.db import models

# Create your models here.


class Category(models.Model):
    catname=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.catname