from django import forms
from . import models
from datetime import date


class Product(forms.Form):
    name = forms.CharField(label='Наименование товара',
                           max_length=30)
    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.FloatField(label='Цена за ед.')
    quantity = forms.IntegerField(label='Количество')
    date_reg = forms.DateField(label='Дата поступления',
                               initial=date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    image = forms.ImageField(label='Фотография товара (не обязательно)',
                             required=False)


class ProductUpdate(forms.Form):
    product_update = forms.ModelChoiceField(label='Выберете товар',
                                            queryset=models.Product.objects.all(),
                                            empty_label='выберете товар')
    name = forms.CharField(label='Наименование товара',
                           max_length=30)
    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.FloatField(label='Цена за ед.')
    quantity = forms.IntegerField(label='Количество')
    date_reg = forms.DateField(label='Дата поступления',
                               initial=date.today,
                                   widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    image = forms.ImageField(label='Фотография товара (не обязательно)',
                             required=False)