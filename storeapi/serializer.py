from rest_framework import serializers
from storeadmin import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Categories
        fields="__all__"

class ProductSerializer(serializers.ModelSerializer):
    category=serializers.CharField(read_only=True)

    class Meta:
        model=models.Products
        fields="__all__"

    def create(self, validated_data):
        category=self.context.get("category")
        return models.Products.objects.create(**validated_data,category=category)

    def update(self, instance, validated_data):
        category=self.context.get("category")
        instance.category=category
        instance.product_name=validated_data.get("product_name")
        instance.product_image=validated_data.get("product_image")
        instance.price=validated_data.get("price")
        instance.description=validated_data.get("description")
        instance.save()
        return instance


class CartSerializer(serializers.ModelSerializer):
    product=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=models.Carts
        fields="__all__"

    def create(self, validated_data):
        product=self.context.get("product_name")
        user=self.context.get("user")
        return models.Carts.objects.create(**validated_data,product=product,user=user)

class OrderSerializer(serializers.ModelSerializer):
    product=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=models.Orders
        fields="__all__"

    def create(self, validated_data):
        product=self.context.get("product_name")
        user=self.context.get("user")
        return models.Orders.objects.create(**validated_data,product=product,user=user)

    def update(self, instance, validated_data):
        instance.status=validated_data.get("status")
        instance.save()
        return instance

class ReviewSerializer(serializers.ModelSerializer):
    product=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=models.Reviews
        fields="__all__"

    def create(self, validated_data):
        product=self.context.get("product_name")
        user=self.context.get("user")
        return models.Reviews.objects.create(**validated_data,product=product,user=user)

    def update(self, instance, validated_data):
        instance.comments=validated_data.get("comments")
        instance.rating=validated_data.get("rating")
        instance.save()
        return instance
