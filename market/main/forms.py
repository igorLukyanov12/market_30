from django import forms
from django.core.exceptions import ValidationError

from main.models import Product


def valid_name(name):
    if name == 'Johan':
        print(name)
    else:
        raise ValidationError('Имя не Johan')
class CategoryForm(forms.Form):
    name = forms.CharField(label='Логин', max_length=100, validators=[valid_name])
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    price = forms.DecimalField(max_digits=8, decimal_places=2)

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image', 'categories']

