from django.db import models

# Create your models here.


class Product(models.Model):
    productname=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.productname