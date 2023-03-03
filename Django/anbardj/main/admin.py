# Register your models here.
from django.contrib import admin

from . models import Brands, Clients, Ishciler , Products, Orders, Expenses , Ishciler, Senedler

admin.site.register(Brands)

admin.site.register(Clients)

admin.site.register(Products)

admin.site.register(Orders)

admin.site.register(Expenses)

admin.site.register(Ishciler)

admin.site.register(Senedler)

