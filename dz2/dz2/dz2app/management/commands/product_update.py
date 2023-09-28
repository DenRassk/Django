import decimal

from django.core.management.base import BaseCommand

from dz2app.models import Product


class Command(BaseCommand):
    help = "Изменение данных о товаре по его ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID товара')
        parser.add_argument('name', type=str, help='Название товара')
        parser.add_argument('description', type=str, help='Описание товара')
        parser.add_argument('price', type=decimal.Decimal, help='Стоимость за единицу')
        parser.add_argument('quantity', type=decimal.Decimal, help='Количество')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            name = kwargs.get('name')
            description = kwargs.get('description')
            price = kwargs.get('price')
            quantity = kwargs.get('quantity')
            if name is not None:
                product.name = name
            if description is not None:
                product.description = description
            if price is not None:
                product.price = price
            if quantity is not None:
                product.quantity = quantity
            product.save()
            self.stdout.write(f'Новые данные {product}')
        else:
            self.stdout.write(f'Товар с ID {pk} не найден!')