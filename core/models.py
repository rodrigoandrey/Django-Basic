from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Stock')

    def __str__(self):
        return self.name


class Client(models.Model):
    firstname = models.CharField('First Name', max_length=100)
    lastname = models.CharField('Last Name', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
