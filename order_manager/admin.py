from django.contrib import admin
from .models import UserAccount, Price, Product, Dispensary, Order

admin.site.register(UserAccount)
admin.site.register(Price)
admin.site.register(Product)
admin.site.register(Dispensary)
admin.site.register(Order)
