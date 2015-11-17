from django.db import models

class Shelf(models.Model):
    col = models.CharField(max_length=4)
    row = models.CharField(max_length=4)
    major_id = models.DecimalField(max_digits=20, decimal_places=10)
    minor_id = models.CharField(max_length=20)
