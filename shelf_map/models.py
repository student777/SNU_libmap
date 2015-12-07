from django.db import models
import re

class Shelf(models.Model):
    room_num = models.CharField(max_length=2)
    col = models.CharField(max_length=4)
    row = models.CharField(max_length=4)
    major_id = models.DecimalField(max_digits=11, decimal_places=7)
    minor_id = models.CharField(max_length=20)
    
    # ex) "대810" : major_leadingChr - True, major_bigBook - True
    # ex) "K809" : major_leadingChr - True, major_bigBook - False
    major_leadingChr = models.BooleanField()
    major_bigBook = models.BooleanField()

    class Meta:
        ordering = ('major_id', 'minor_id', )

    def __str__(self):
        return str(self.major_id) + ' ' + self.minor_id
        

def create_shelf(room_num, col, row, major_id, minor_id):
    IGNORE_CHRSET = ["", "-", "/"]
    # without encapsulation...
    
    a = Shelf()

    # Does major_num contain character?
    if type(major_id) == type(0.0):
        # Only consisted with numbers
        a.major_leadingChr = False
        a.major_bigBook = False
        a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, major_id, minor_id
        a.save()
        
    elif type(major_id) == type("asd"):
        # Containing characters
        if major_id in IGNORE_CHRSET:
            # Ignore
            pass
        
        elif major_id[0] == "대":
            # Big book
            a.major_leadingChr = True
            a.major_bigBook = True
            try:
                a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, float(major_id[1:]), minor_id
                a.save()
            except:
                pass
                # 혹시나 잘못 입력된 데이터 (디버깅)
                #print(room_num, col, row, major_id)
        
        elif bool(re.match("[a-zA-Z]", major_id[0])):
            a.major_leadingChr = True
            a.major_bigBook = False
            
            try:
                a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, float(major_id[1:]), minor_id
                a.save()
            except:
                pass

        elif major_id == 'KOCKA':
            a.major_leadingChr = True
            a.major_bigBook = False
            try:
                a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, float(major_id[5:]), minor_id
                a.save()
            except:
                pass
        else:
            pass
    
    else:
        pass