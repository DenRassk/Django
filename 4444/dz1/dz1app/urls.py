from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Начальная страница сайта'),
    path('about/', views.about, name='Обо мне'),
]