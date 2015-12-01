from django.db import models


class Shelf_1(models.Model):
    col = models.CharField(max_length=4)
    row = models.CharField(max_length=4)
    major_id = models.DecimalField(max_digits=11, decimal_places=7)
    minor_id = models.CharField(max_length=20)

    class Meta:
        ordering = ('major_id', 'minor_id', )

    def __str__(self):
        return str(self.major_id) + ' ' + self.minor_id


class Shelf_2(models.Model):
    col = models.CharField(max_length=4)
    row = models.CharField(max_length=4)
    major_id = models.DecimalField(max_digits=11, decimal_places=7)
    minor_id = models.CharField(max_length=20)

    class Meta:
        ordering = ('major_id', 'minor_id', )

    def __str__(self):
        return str(self.major_id) + ' ' + self.minor_id


class Shelf_3(models.Model):
    col = models.CharField(max_length=4)
    row = models.CharField(max_length=4)
    major_id = models.DecimalField(max_digits=11, decimal_places=7)
    minor_id = models.CharField(max_length=20)

    class Meta:
        ordering = ('major_id', 'minor_id', )

    def __str__(self):
        return str(self.major_id) + ' ' + self.minor_id


class Shelf_4(models.Model):
    col = models.CharField(max_length=4)
    row = models.CharField(max_length=4)
    major_id = models.DecimalField(max_digits=11, decimal_places=7)
    minor_id = models.CharField(max_length=20)

    class Meta:
        ordering = ('major_id', 'minor_id', )

    def __str__(self):
        return str(self.major_id) + ' ' + self.minor_id


class Shelf_5(models.Model):
    col = models.CharField(max_length=4)
    row = models.CharField(max_length=4)
    major_id = models.DecimalField(max_digits=11, decimal_places=7)
    minor_id = models.CharField(max_length=20)

    class Meta:
        ordering = ('major_id', 'minor_id', )

    def __str__(self):
        return str(self.major_id) + ' ' + self.minor_id


class Shelf_6(models.Model):
    col = models.CharField(max_length=4)
    row = models.CharField(max_length=4)
    major_id = models.DecimalField(max_digits=11, decimal_places=7)
    minor_id = models.CharField(max_length=20)

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


def create_shelf_1(col, row, major_id, minor_id):
    a = Shelf_1(col=col, row=row, major_id=major_id, minor_id=minor_id)
    a.save()


def create_shelf_2(col, row, major_id, minor_id):
    a = Shelf_2(col=col, row=row, major_id=major_id, minor_id=minor_id)
    a.save()


def create_shelf_3(col, row, major_id, minor_id):
    a = Shelf_3(col=col, row=row, major_id=major_id, minor_id=minor_id)
    a.save()


def create_shelf_4(col, row, major_id, minor_id):
    a = Shelf_4(col=col, row=row, major_id=major_id, minor_id=minor_id)
    a.save()


def create_shelf_5(col, row, major_id, minor_id):
    a = Shelf_5(col=col, row=row, major_id=major_id, minor_id=minor_id)
    a.save()


def create_shelf_6(col, row, major_id, minor_id):
    a = Shelf_6(col=col, row=row, major_id=major_id, minor_id=minor_id)
    a.save()

def create_shelf_7(col, row, major_id, minor_id):
    a = Shelf_7(col=col, row=row, major_id=major_id, minor_id=minor_id)
    a.save()

