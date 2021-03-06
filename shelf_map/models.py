from django.db import models
import re


class Shelf(models.Model):
    room_num = models.CharField(max_length=4)
    col = models.CharField(max_length=4)
    row = models.CharField(max_length=4)
    major_id = models.DecimalField(max_digits=11, decimal_places=7)
    minor_id = models.CharField(max_length=20)
    major_leadingChr = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        ordering = ('major_id', 'minor_id',)

    def __str__(self):
        return str(self.major_id) + ' ' + self.minor_id


def create_shelf(room_num, col, row, major_id, minor_id):
    ignore_charset = ["", "-", "/"]

    a = Shelf()

    if isinstance(major_id, float):
        a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, major_id, minor_id
        a.save()

    elif isinstance(major_id, str):
        if major_id in ignore_charset:
            pass

        elif major_id[0] == "대":
            a.major_leadingChr = "대"
            try:
                a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, float(major_id[1:]), minor_id
                a.save()
            except Exception as e:
                print(room_num, col, row, major_id, minor_id, 'error1', e)

        elif major_id.startswith('KOCKA'):
            a.major_leadingChr = 'KOCKA'
            try:
                a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, float(major_id[6:]), minor_id
                a.save()
            except Exception as e:
                print(room_num, col, row, major_id, minor_id, 'error2', e)

        elif bool(re.match("[a-zA-Z]", major_id[0])):
            a.major_leadingChr = major_id[0]
            try:
                a.room_num, a.col, a.row, a.major_id, a.minor_id = room_num, col, row, float(major_id[1:]), minor_id
                a.save()
            except Exception as e:
                print(room_num, col, row, major_id, minor_id, 'error3', e)

        else:
            print(room_num, col, row, major_id, minor_id, 'error4')

    else:
        print(room_num, col, row, major_id, minor_id, 'error5')
