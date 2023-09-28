from datetime import datetime, timedelta

from django.shortcuts import render


from .models import User, Order

# Create your views here.


def index(request):
    users = User.objects.all()
    context = {'title': 'Учебный сайт - главная',
               'users': users}
    return render(request,'dz2app/index.html', context)


def user_order(request, user_id):
    user = User.objects.filter(pk=user_id).first()

    context = {'user_name': user.name,
               'user_id': user_id
               }
    return render(request, 'dz2app/user_orders.html', context)


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
