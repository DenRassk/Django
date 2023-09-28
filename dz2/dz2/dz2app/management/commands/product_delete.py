from django.core.management.base import BaseCommand

from dz2app.models import Product


class Command(BaseCommand):
    help = "Удаление товара по его ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID товара')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.delete()
            self.stdout.write(f'Товар с ID {pk} удалён!')
        else:
            self.stdout.write(f'Товар с ID {pk} не найден!')