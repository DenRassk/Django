from datetime import date

from django.db import models
from django.urls import reverse


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=12)
    address = models.CharField(max_length=50)
    date_reg = models.DateField(default=date.today())

    def __str__(self):
        return f'пользователь: {self.name}, эл. почта: {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=8, decimal_places=3) # на случай если количество - вес в КГ до грамма
    date_reg = models.DateField(default=date.today())
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return f'Товар: {self.name} Цена за 1 единицу: {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(default=date.today())
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Дата покупки: {self.date_ordered} Стоимость покупки: {self.total_price}'
