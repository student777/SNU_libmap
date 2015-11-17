from django.db import models


class Shelf(models.Model):
    col = models.CharField(max_length=4)
    row = models.CharField(max_length=4)
    major_id = models.DecimalField(max_digits=20, decimal_places=10)
    minor_id = models.CharField(max_length=20)

    def __str__(self):
        return self.col + self.row + '/' + str(self.major_id) + ' ' + self.minor_id


def create_shelf(col, row, major_id, minor_id):
    a = Shelf(col=col, row=row, major_id=major_id, minor_id=minor_id)
    a.save()
