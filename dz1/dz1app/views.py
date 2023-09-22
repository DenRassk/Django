from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Домашнее задание к 1 семинару</title>
    </head>
    <body>
        <h2>О сайте</h2>
        <p>Мой первый сайт на Django</p>

        <footer>
            <p>Мои координаты на планете Земля:</p>
            <p style="text-indent: 25px;">66.113269, 76.691245</p>
            <p>Подробный маршрут во Вселенной - на странице:</p>
            <a href="about">Обо мне</a>
        </footer>
    </body>
    </html>
    """
    logger.info('Кто то зашёл на мой сайт')
    return HttpResponse(html)


def about(request):
    html = """<!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Обо мне</title>
    </head>
    <body>
        <header>
            <h2>Привет! <br>Я житель этой Вселенной!</h2>
        </header>

        <main>
            <p>Как добраться:
            <br>комплекс сверхскоплений Рыб-Кита
            <br>сверхскопление Ланиакея,
            <br>сверхскопление Девы,
            <br>скопление Девы,
            <br>Местная группа галактик,
            <br>галактика Млечный Путь,
            <br>галактический рукав Ориона,
            <br>Солнечная система,
            <br>планета Земля</p>
        </main>
        <footer>
            <a href="/">На главную</a>
            <p>Используется с моего разрешения!</p>
        </footer>
    </body>
    </html>
    """
    logger.info('Кто-то открыл страницу Обо мне')
    return HttpResponse(html)
