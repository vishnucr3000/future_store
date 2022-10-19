from django.shortcuts import render
from storeadmin import models
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from storeapi import serializer
from storeadmin.models import Categories,Products
from rest_framework.decorators import action
from rest_framework import authentication
from rest_framework import permissions
from django.contrib.auth.models import User


# Create your views here.
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer

class CategoryView(ModelViewSet):
    queryset = models.Categories.objects.all()
    serializer_class = serializer.CategorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]

    @action(methods=["post"],detail=True)
    def add_product(self,request,*args,**kwargs):
        categoryid=kwargs.get("pk")
        category=Categories.objects.get(id=categoryid)
        serialize=serializer.ProductSerializer(data=request.data,context={"category":category})
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data)
        else:
            return Response(data=serialize.errors)

    @action(methods=["put"],detail=True)
    def edit_product(self,request,*args,**kwargs):
        category_id=kwargs.get("pk")
        category=Categories.objects.get(id=category_id)
        instance_id = request.query_params.get("product_id")
        instance=Products.objects.get(id=instance_id)
        print(instance)
        serialize=serializer.ProductSerializer(instance,data=request.data,context={"category":category})
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data)
        else:
            return Response(data=serialize.errors)

class ProductsView(ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializer.ProductSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        return Response("Not Allowed")
    def update(self, request, *args, **kwargs):
        return Response("Not Allowed")

    @action(methods=["post"],detail=True)
    def add_to_cart(self,request,*args,**kwargs):
        product_id=kwargs.get("pk")
        product=Products.objects.get(id=product_id)
        user=request.user
        serialize=serializer.CartSerializer(data=request.data,context={"product_name":product,"user":user})
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data)
        else:
            return Response(data=serialize.errors)
    @action(methods=["put"],detail=True)
    def edit_cart(self,request,*args,**kwargs):
        product_id=kwargs.get("pk")
        product=Products.objects.get(id=product_id)
        instance=models.Carts.objects.get(request.query_params.get("cart_id"))
        serialize=serializer.CartSerializer(instance,data=request.data,context={"product_name":product})
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data)
        else:
            return Response(data=serialize.errors)

    @action(methods=["post"],detail=True)
    def add_order(self,request,*args,**kwargs):
        product_id=kwargs.get("pk")
        product=Products.objects.get(id=product_id)
        user=request.user
        serialize=serializer.OrderSerializer(data=request.data,context={"product_name":product,"user":user})
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data)
        else:
            return Response(data=serialize.errors)

    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        product_id=kwargs.get("pk")
        product=models.Products.objects.get(id=product_id)
        user=request.user
        serialize=serializer.ReviewSerializer(data=request.data,context={"product_name":product,"user":user})
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data)
        else:
            return Response(data=serialize.errors)



class CartsView(ModelViewSet):
    queryset = models.Carts.objects.all()
    serializer_class = serializer.CartSerializer

    def create(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def update(self, request, *args, **kwargs):
        return Response("Not Allowed")

class OrderView(ModelViewSet):
    queryset = models.Orders.objects.all()
    serializer_class = serializer.OrderSerializer

    def create(self, request, *args, **kwargs):
        return Response("Not Allowed")

class ReviewView(ModelViewSet):
    queryset = models.Reviews.objects.all()
    serializer_class = serializer.ReviewSerializer

    def create(self, request, *args, **kwargs):
        return Response("Not Allowed")









