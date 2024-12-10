from django.contrib import admin
from .models import *
from .models import Brand, Category, Product, Order, Coupon, Setting

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Coupon)
admin.site.register(Setting)

# Register your models here.
