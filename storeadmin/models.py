from django.db import models
from django.contrib.auth.models import User
from django.core import validators

# Create your models here.

class Categories(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name=models.CharField(max_length=50)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE,related_name='products')
    product_image=models.ImageField(upload_to="static/images/product_images",null=True)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.product_name

class Carts(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)
    options=(
        ("in-cart","incart"),
        ("order_placed","order_placed"),
        ("cancelled","cancelled"),
    )
    status=models.CharField(max_length=20,choices=options,default="in-cart")

class Orders(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("await-shipping","await-shipping"),
        ("dispatched","dispatched"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
    )
    status=models.CharField(max_length=20,choices=options,default="await-shipping")

class Reviews(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comments=models.CharField(max_length=250)
    rating=models.FloatField(validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)])


