from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    cusine = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name + " : " + self.cusine