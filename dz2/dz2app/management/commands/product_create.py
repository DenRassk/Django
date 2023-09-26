import decimal

from django.core.management.base import BaseCommand

from dz2app.models import Product


class Command(BaseCommand):
    help = "Создание нового товара"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Название товара')
        parser.add_argument('description', type=str, help='Описание товара')
        parser.add_argument('price', type=decimal.Decimal, help='Стоимость за единицу')
        parser.add_argument('quantity', type=decimal.Decimal, help='Количество')


    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')
        product = Product(name=name,
                    description=description,
                    price=price,
                    quantity=quantity
                    )
        product.save()
        self.stdout.write(f'Создан {product}')
