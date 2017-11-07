from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=20)
    max_storage_temperature = models.FloatField(default=2)
    min_storage_temperature = models.FloatField(default=-10)
    max_storage_time = models.IntegerField()
    max_storage_available = models.IntegerField()
    storage_filled = models.IntegerField()

    def __str__(self):
        return self.name


class Stock(models.Model):
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item.name + '-' + str(self.quantity)
