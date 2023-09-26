from django.core.management.base import BaseCommand

from dz2app.models import User


class Command(BaseCommand):
    help = "Создание нового пользователя"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Имя пользователя')
        parser.add_argument('email', type=str, help='Электронная почта')
        parser.add_argument('tel', type=str, help='Телефон')
        parser.add_argument('address', type=str, help='Адрес')


    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        tel = kwargs.get('tel')
        address = kwargs.get('address')
        user = User(name=name,
                    email=email,
                    tel=tel,
                    address=address
                    )
        user.save()
        self.stdout.write(f'Создан {user}')
