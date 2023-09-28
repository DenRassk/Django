from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Начальная страница'),
    path('user/<int:user_id>/orders/', views.user_order, name='Заказы пользователя'),
    path('user/<int:user_id>/orders/<int:range_>', views.user_order_range, name='Заказы пользователя за период'),
]