from django.db import models
import re

class Shelf(models.Model):
    room_num = models.DecimalField(max_digits = 2, decimal_places=2)
    col = models.CharField(max_length=4)
    row = models.CharField(max_length=4)
    major_id = models.DecimalField(max_digits=11, decimal_places=7)
    minor_id = models.CharField(max_length=20)
    
    # ex) "대810" : major_leadingChr - True, major_bigBook - True
    # ex) "K809" : major_leadingChr - True, major_bigBook - False
    major_leadingChr = models.BooleanFiled()
    major_bigBook = models.BooleanFiled()

    class Meta:
        ordering = ('major_id', 'minor_id', )

    def __str__(self):
        return str(self.major_id) + ' ' + self.minor_id
        
        
class Shelf_7(models.Model):
    col = models.CharField(max_length=4)
    row = models.CharField(max_length=4)
    major_id = models.DecimalField(max_digits=11, decimal_places=7)
    minor_id = models.CharField(max_length=20)

    class Meta:
        ordering = ('major_id', 'minor_id', )

    def __str__(self):
        return str(self.major_id) + ' ' + self.minor_id

def create_shelf(room_num, col, row, major_id, minor_id):
    # without encapsulation...
    a = Shelf()
    
    # Have leading character?
    if bool(re.match("[0-9]", major_id[0])):
        a.major_leadingChr = False
        a.major_bigBook = False
        # Can assign major_id freely
        a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, major_id, minor_id
        
    else:
        a.major_leadingChr = True
        # If it starts with "대", then it is big book.
        a.majorbigBook = True if major_id[0] == "대" else False
        # Cannot assign major_id freely, remove first character
        a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, major_id[1:], minor_id

    a.save()

def create_shelf_7(col, row, major_id, minor_id):
    a = Shelf_7(col=col, row=row, major_id=major_id, minor_id=minor_id)
    a.save()

