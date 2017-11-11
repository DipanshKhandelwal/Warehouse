from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=20)
    max_storage_temperature = models.FloatField(default=2)
    min_storage_temperature = models.FloatField(default=-10)
    max_storage_time = models.IntegerField()
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Stock(models.Model):
    master = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()
    stored_date = models.DateField()

    def __str__(self):
        return self.item.name + '-' + str(self.quantity)


class Farmer(models.Model):
    user = models.OneToOneField(User)
    address = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)  # validators should be a list

    def __str__(self):
        return self.user.username + '-' + self.phone_number
