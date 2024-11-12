from django.db import models


class Buyer(models.Model):

    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2, max_digits=9)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):

    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=9)
    size = models.DecimalField(decimal_places=1, max_digits=5)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title
