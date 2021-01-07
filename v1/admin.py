from django.contrib import admin
from v1.models import Customer, Cake, Recipe, Order

# Register your models here.
admin.site.register((Customer, Cake, Recipe, Order))
