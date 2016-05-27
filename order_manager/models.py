from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    dl = models.CharField(max_length=16, unique=True)
    phone = models.CharField(max_length=10, unique=True)


class Price(models.Model):
    amount = models.CharField(max_length=15)
    weight = models.CharField(max_length=20)


class Product(models.Model):
    strain = models.CharField(max_length=100)
    description = models.TextField()
    prices = models.ManyToManyField(Price)


class Dispensary(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=80)
    phone = models.CharField(max_length=10)
    hours = models.CharField(max_length=50)
    menu = models.ManyToManyField(Product)


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_dl = models.ForeignKey(UserAccount)
    products = models.ManyToManyField(Product)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    time_ordered = models.DateTimeField(default=timezone.now)
    time_pickup = models.DateTimeField()
