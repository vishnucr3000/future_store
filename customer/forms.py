from django import  forms
from storeadmin import models

class CartsForm(forms.ModelForm):
    qty=forms.CharField(label="",widget=forms.NumberInput(attrs={"class":"form-control", "value":1}))
    class Meta:
        model=models.Carts
        fields=["qty"]
