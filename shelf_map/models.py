from django.db import models
import re


class Shelf(models.Model):
    room_num = models.CharField(max_length=2)
    col = models.CharField(max_length=4)
    row = models.CharField(max_length=4)
    major_id = models.DecimalField(max_digits=11, decimal_places=7)
    minor_id = models.CharField(max_length=20)
    major_leadingChr = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        ordering = ('major_id', 'minor_id', )

    def __str__(self):
        return str(self.major_id) + ' ' + self.minor_id


def create_shelf(room_num, col, row, major_id, minor_id):
    IGNORE_CHRSET = ["", "-", "/"]

    a = Shelf()

    if type(major_id) == type(0.0):
        a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, major_id, minor_id
        a.save()

    elif type(major_id) == type("asd"):
        if major_id in IGNORE_CHRSET:
            pass

        elif major_id[0] == "대":
            a.major_leadingChr = "대"
            try:
                a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, float(major_id[1:]), minor_id
                a.save()
            except:
                print(room_num, col, row, major_id, minor_id, 'label1')

        elif major_id.startswith('KOCKA'):
            a.major_leadingChr = 'KOCKA'
            try:
                a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, float(major_id[6:]), minor_id
                a.save()
            except:
                print(room_num, col, row, major_id, minor_id, 'label2')

        elif bool(re.match("[a-zA-Z]", major_id[0])):
            a.major_leadingChr = major_id[0]
            try:
                a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, float(major_id[1:]), minor_id
                a.save()
            except:
                print(room_num, col, row, major_id, minor_id, 'label3')

        else:
            print(room_num, col, row, major_id, minor_id, 'label4')

    else:
        print(room_num, col, row, major_id, minor_id, 'label5')
