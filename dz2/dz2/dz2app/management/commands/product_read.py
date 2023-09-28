from django.core.management.base import BaseCommand

from dz2app.models import Product


class Command(BaseCommand):
    help = "Поиск и вывод данных о пользователе по его ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID пользователя')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            self.stdout.write(f'{product}')
        else:
            self.stdout.write(f'Пользователь с ID {pk} не найден!')
