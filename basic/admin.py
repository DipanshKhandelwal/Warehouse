from django.contrib import admin
from .models import Item, Stock, Farmer

# Register your models here.
my_models = [Item, Stock, Farmer]
admin.site.register(my_models)
