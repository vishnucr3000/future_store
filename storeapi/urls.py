from django.urls import path
from rest_framework.routers import DefaultRouter
from storeapi import views
from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()

router.register("v1/categories",views.CategoryView,basename="categories")
router.register("v1/products",views.ProductsView,basename="products")
router.register("v1/users",views.UserView,basename="users")
router.register("v1/carts",views.CartsView,basename="carts")
router.register("v1/orders",views.OrderView,basename="orders")
router.register("v1/reviews",views.ReviewView,basename="reviews")


urlpatterns=[

path("v1/get_token/",ObtainAuthToken.as_view(),name="get_token")

]+router.urls

