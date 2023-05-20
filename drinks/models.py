from django.db import models

class Drink(models.Model):
    title= models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title+ " "+self.description