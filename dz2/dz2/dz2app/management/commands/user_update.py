from django.core.management.base import BaseCommand

from dz2app.models import User


class Command(BaseCommand):
    help = "Изменение данных о пользователе по его ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=str, help='ID пользователя')
        parser.add_argument('name', type=str, help='Имя пользователя')
        parser.add_argument('email', type=str, help='Электронная почта')
        parser.add_argument('tel', type=str, help='Телефон')
        parser.add_argument('address', type=str, help='Адрес')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            name = kwargs.get('name')
            email = kwargs.get('email')
            tel = kwargs.get('tel')
            address = kwargs.get('address')
            if name is not None:
                user.name = name
            if email is not None:
                user.email = email
            if tel is not None:
                user.tel = tel
            if address is not None:
                user.address = address
            user.save()
            self.stdout.write(f'Новые данные {user}')
        else:
            self.stdout.write(f'Пользователь с ID {pk} не найден!')