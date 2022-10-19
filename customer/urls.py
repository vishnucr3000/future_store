from django.urls import path
from customer import views

urlpatterns=[
    path("",views.IndexView.as_view(),name="index"),
    path("carts/<int:id>",views.CartAddView.as_view(),name="add-cart"),
    path("carts/list/",views.CartListView.as_view(),name="list-cart"),
    path("carts/remove/<int:id>",views.remove_cart,name="remove-cart"),
    path("carts/checkout/<int:cid>/<int:pid>/",views.OrderView.as_view(),name="checkout"),
    path("orders/",views.OrderListView.as_view(),name="orders"),
]