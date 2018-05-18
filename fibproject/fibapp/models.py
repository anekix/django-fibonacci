from django.db import models

# Create your models here.
from django.db import models


class FibonacciNumber(models.Model):
    nth_term = models.IntegerField()
    value = models.TextField()
