import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from dz2app.models import User, Product, Order


class Command(BaseCommand):
    help = "Генератор тестовых данных (пользователь, товар, покупки)"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(1, count + 1):
            user = User(name=f'Name{i}',
                        email=f'mail{i}@mail.ru',
                        tel=f'+798765432{i}',
                        address=f'г.Воронеж, ул. Лизюкова, д. {i+10}'
                        )

            user.save()

        for j in range(1, count + 1):
            product = Product(name=f'Товар_{j}',
                              description=f'Супер-пупер товар_{j}',
                              price=1.05*j,
                              quantity=21*j
                              )
            product.save()

        for i in range(1, count + 1):
            user = User.objects.filter(pk=i).first()
            for _ in range(1, random.randint(2, count)):
                total_price = 0
                order = Order(customer=user,
                              date_ordered=timezone.now() - timedelta(days=random.randint(1, 500)))
                for j in range(1, random.randint(2, count)):
                    product = Product.objects.filter(pk=j).first()
                    total_price += product.price
                    order.total_price = total_price
                    order.save()
                    order.products.add(product)
