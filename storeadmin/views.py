from django.shortcuts import render, redirect
from storeadmin import models
from django.views.generic import CreateView, ListView, DetailView, UpdateView, FormView, TemplateView, View
from storeadmin import forms
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

@method_decorator(login_required, name="dispatch")
class RegistrationView(CreateView):
    model = User
    form_class = forms.RegistrationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            if user:
                login(request, user)
                if user.is_superuser:
                    return redirect("home")
                else:
                    return redirect("index")
            else:
                return redirect("login")


@login_required()
def logoutview(request):
    logout(request)
    return redirect("login")


@method_decorator(login_required, name="dispatch")
class HomeView(TemplateView):
    template_name = "home.html"
    extra_context = {"category_count": models.Categories.objects.all().count(),
                     "product_count": models.Products.objects.all().count(), \
                     "order_count": models.Orders.objects.exclude(status="cancelled").count(),
                     "cancelled_order_count": models.Orders.objects.filter(status="cancelled").count()}


@method_decorator(login_required, name="dispatch")
class CategoryAddView(CreateView):
    model = models.Categories
    form_class = forms.CategoryAddForm
    template_name = "add_category.html"
    success_url = reverse_lazy("list_categories")


@method_decorator(login_required, name="dispatch")
class CategoryListView(ListView):
    model = models.Categories
    template_name = "category_list.html"
    context_object_name = "categories"


@method_decorator(login_required, name="dispatch")
class CategoryDetailView(DetailView):
    model = models.Categories
    template_name = "category_details.html"
    context_object_name = "category"
    pk_url_kwarg = "id"


@method_decorator(login_required, name="dispatch")
class CategoryEditView(UpdateView):
    model = models.Categories
    form_class = forms.CategoryAddForm
    template_name = "edit-category.html"
    context_object_name = "category"
    pk_url_kwarg = "id"

    def get_success_url(self):
        id = self.kwargs.get("id")
        return reverse("category_details", kwargs={"id": id})


@method_decorator(login_required, name="dispatch")
class ProductAddView(CreateView):
    model = models.Products
    form_class = forms.ProductsForm
    template_name = "add-product.html"
    context_object_name = "product"
    success_url = reverse_lazy("list-products")


@method_decorator(login_required, name="dispatch")
class ProductListView(ListView):
    model = models.Products
    template_name = "product-list.html"
    context_object_name = "products"


@method_decorator(login_required, name="dispatch")
class ProductDetailView(DetailView):
    model = models.Products
    template_name = "product-details.html"
    context_object_name = "product"
    pk_url_kwarg = "id"


@method_decorator(login_required, name="dispatch")
class ProductEditView(UpdateView):
    model = models.Products
    form_class = forms.ProductsForm
    template_name = "edit-products.html"
    context_object_name = "products"
    pk_url_kwarg = "id"

    def get_success_url(self):
        id = self.kwargs.get("id")
        return reverse("product-details", kwargs={"id": id})


class OrderListView(ListView):
    model = models.Orders
    context_object_name = "orders"
    template_name = "order-process.html"
    queryset = models.Orders.objects.exclude(status="cancelled")


class OrderCancelledView(ListView):
    model = models.Orders
    context_object_name = "orders"
    template_name = "cancelled-orders.html"
    queryset = models.Orders.objects.filter(status="cancelled")


class EditOrderView(UpdateView):
    model = models.Orders
    template_name = "edit-orders.html"
    form_class = forms.OrderProcessForm
    context_object_name = "order"
    pk_url_kwarg = "id"
