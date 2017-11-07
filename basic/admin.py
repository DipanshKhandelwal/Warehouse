from django.contrib import admin
from .models import Item, Stock

# Register your models here.
my_models = [Item, Stock]
admin.site.register(my_models)
