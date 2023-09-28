from django.core.management.base import BaseCommand

from dz2app.models import User


class Command(BaseCommand):
    help = "Поиск и вывод данных о пользователе по его ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID пользователя')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            self.stdout.write(f'{user}')
        else:
            self.stdout.write(f'Пользователь с ID {pk} не найден!')
