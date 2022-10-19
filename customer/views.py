from django.shortcuts import render,redirect
from storeadmin import models
from django.views.generic import CreateView,FormView,TemplateView,ListView,UpdateView
from customer import forms
from storeadmin.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required,name="dispatch")
class IndexView(TemplateView):
    template_name = "dashboard.html"
    extra_context = {"products":models.Products.objects.all()}

@method_decorator(login_required,name="dispatch")
class CartAddView(FormView):
    template_name = "add-to-cart.html"
    form_class =forms.CartsForm


    def get(self,request,*args,**kwargs):
        product_id=kwargs.get("id")
        product=models.Products.objects.get(id=product_id)
        return render(self.request,self.template_name,{"form":forms.CartsForm(),"product":product})

    def post(self, request, *args, **kwargs):
        product_id=kwargs.get("id")
        product=models.Products.objects.get(id=product_id)
        qty=request.POST.get("qty")
        user=request.user
        models.Carts.objects.create(product=product,user=user,qty=qty)
        return redirect("index")

@method_decorator(login_required,name="dispatch")
class CartListView(ListView):
    model = models.Carts
    template_name = "list-cart.html"
    context_object_name = "carts"

@method_decorator(login_required,name="dispatch")
def remove_cart(self,*args,**kwargs):
    cart_id=kwargs.get("id")
    cart=models.Carts.objects.get(id=cart_id)
    cart.status="cancelled"
    cart.save()
    return redirect("list-cart")

@method_decorator(login_required,name="dispatch")
class OrderView(FormView):
    def get(self,request,*args,**kwargs):
        product_id=kwargs.get("pid")
        product=models.Products.objects.get(id=product_id)
        return render(request,template_name="add-to-cart.html",context={"product":product,"form":forms.CartsForm})

    def post(self, request, *args, **kwargs):
        cart_id=kwargs.get("cid")
        cart=models.Carts.objects.get(id=cart_id)
        product_id=kwargs.get("pid")
        print(product_id)
        product=models.Products.objects.get(id=product_id)
        user=request.user
        models.Orders.objects.create(product=product,user=user)
        cart.status="order_placed"
        cart.qty=request.POST.get("qty")
        cart.save()
        return redirect("list-cart")

@method_decorator(login_required,name="dispatch")
class OrderListView(ListView):
    model = models.Orders
    template_name = "order-list.html"
    context_object_name = "orders"









