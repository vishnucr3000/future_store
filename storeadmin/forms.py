from django import forms
from storeadmin import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=50,label="Enter Password",help_text="Must be 8 Charactors contains Upper Case, Lower Case Number and a special charactor",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(max_length=50,label="Confirm Password",help_text="Enter the same password as before, for verification.",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),

        }

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),error_messages={"errors":"sfsdfsdf"} )
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    def clean(self):
        cleaned_data=super().clean()
        username=self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("User Name is required")





class CategoryAddForm(forms.ModelForm):
    class Meta:
        model=models.Categories
        fields="__all__"
        widgets={
            "category_name":forms.TextInput(attrs={"class":"form-control"})
        }

class ProductsForm(forms.ModelForm):

    class Meta:
        model=models.Products
        fields="__all__"
        widgets={
            "product_name":forms.TextInput(attrs={"class":"form-control"}),
            "category":forms.Select(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "product_image":forms.FileInput(attrs={"class":"form-control"}),

        }


class OrderProcessForm(forms.Form):
    options=(
        ("await-shipping","await-shipping"),
        ("dispatched","dispatched"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
    )
    status=forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":"form-control"}))

