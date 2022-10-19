from django.urls import path
from storeadmin import views

urlpatterns = [
    path("signup/", views.RegistrationView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logoutview, name="logout"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("categories/add/", views.CategoryAddView.as_view(), name="add_categories"),
    path("categories/list/", views.CategoryListView.as_view(), name="list_categories"),
    path("categories/edit/<int:id>/", views.CategoryEditView.as_view(), name="edit-categories"),
    path("categories/<int:id>/", views.CategoryDetailView.as_view(), name="category_details"),
    path("products/add/", views.ProductAddView.as_view(), name="add-products"),
    path("products/list/", views.ProductListView.as_view(), name="list-products"),
    path("products/<int:id>/", views.ProductDetailView.as_view(), name="product-details"),
    path("products/edit/<int:id>/", views.ProductEditView.as_view(), name="edit-product"),
    path("orders/", views.OrderListView.as_view(), name="order-process"),
    path("orders/edit/<int:id>/", views.EditOrderView.as_view(), name="edit-order"),
    path("orders/cancelled/", views.OrderCancelledView.as_view(), name="cancelled-order"),

]
