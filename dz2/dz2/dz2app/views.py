from datetime import datetime, timedelta
from pathlib import Path

from django.shortcuts import render
from django.utils import timezone

from . import forms
from .models import User, Order, Product


# Create your views here.


def index(request):
    context = {'title': 'Учебный сайт - главная',
               'header': 'Выберите раздел:',
               'link': '/',
               'text': 'на главную',
               }
    return render(request,'dz2app/index.html', context)


# ДЗ 3 - список пользователей
def users(request):
    users = User.objects.all()
    context = {'title': 'Учебный сайт - главная',
               'users': users,
               'footer_link': '/',
               'footer_link': 'на главную',
               }
    return render(request,'dz2app/users.html', context)

# ДЗ 3 - список заказов пользователя
def user_order(request, user_id):
    user = User.objects.filter(pk=user_id).first()

    context = {'user_name': user.name,
               'user_id': user_id
               }
    return render(request, 'dz2app/user_orders.html', context)

# ДЗ 3 - список заказов отфильтрованый по диапазонам и отсортированный по дате
def user_order_range(request, user_id, range_):
    products = []
    user = User.objects.filter(pk=user_id).first()
    if range_ != 400:
        start = datetime.now() - timedelta(days=range_)
        stop = datetime.now()
        orders = Order.objects.filter(customer=user_id, date_ordered__range=(start, stop)).order_by('-date_ordered')
        title = f'Заказы за последние {range_} дней' if range_ != 365 else f'Заказы за последний год'
    else:
        orders = Order.objects.filter(customer=user_id).order_by('-date_ordered')
        title = f'Все заказы'

    if orders.exists():
        for order in orders:
            for product_tmp in order.products.all():
                products.append([order.date_ordered.strftime('%m.%d.%Y'), product_tmp.name])
    else:
        orders = 0

    context = {'title': title,
               'user_name': user.name,
               'orders': orders,
               'products': products,
    }
    return render(request, 'dz2app/base_orders.html', context)


# дз4 - типа главная старница у товаров
def product_index(request):
    context = {'title': 'Управление товарами',
               'link': '/',
               'text': 'на главную',
               }
    return render(request, 'dz2app/product.html', context)



# дз 4 - форма добавления нового товара
def product_add(request):
    message = ''
    title = 'Добавление нового товара'
    if request.method == 'POST':
        form = forms.Product(request.POST, request.FILES)
        if form.is_valid():
            product = Product(name=form.cleaned_data['name'],
                              description=form.cleaned_data['description'],
                              price=form.cleaned_data['price'],
                              quantity=form.cleaned_data['quantity'],
                              date_reg=timezone.now(),
                              image=form.cleaned_data['image']
                              )
            product.save()
            message = "Товар добавлен!"
    else:
        form = forms.Product()
        message = "Заполните форму:"
    return render(request,
                  'dz2app/product_add.html',
                  {'form': form,
                   'message': message,
                   'title': title,
                   'link': '/product',
                   'text': 'Управление продуктами'}
                  )


# дз 4 - форма изменения данных о товаре
def product_update(request):
    message = ''
    title = 'Обновление данных о товаре'
    if request.method == 'POST':
        form = forms.ProductUpdate(request.POST, request.FILES)
        if form.is_valid():
            pk = form.cleaned_data['product_update'].pk
            product = Product.objects.filter(pk=pk).first()
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            product.date_reg = timezone.now()
            product.image = form.cleaned_data['image']
            product.save()
            message = "Данные о товаре обновлены!"
    else:
        form = forms.ProductUpdate
        message = "Выберите товар и отредактируйте его данные"
    return render(request, 'dz2app/product_update.html',
                  {'form': form,
                   'message': message,
                   'title': title,
                   'link': '/product',
                   'text': 'Управление продуктами'
                   }
                  )


# дз 4 - форма показать все товары
def products_show_all(request):
    message = 'Просмотр списка товаров'
    title = 'Список товаров'
    products = Product.objects.all()
    return render(request, 'dz2app/product_show_all.html',
                  {'products': products,
                   'message': message,
                   'title': title,
                   'link': '/product',
                   'text': 'Управление продуктами'
                   }
                  )
