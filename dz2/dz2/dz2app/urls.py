
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='Начальная страница'),
    path('users/', views.users, name='Пользователя'),
    path('users/user/<int:user_id>/orders/', views.user_order, name='Заказы пользователя'),
    path('users/user/<int:user_id>/orders/<int:range_>', views.user_order_range, name='Заказы пользователя за период'),
    path('product/', views.product_index, name='Работа с товарами - главная'),
    path('product/all/', views.products_show_all, name='Просмотр всех товаров'),
    path('product/add/', views.product_add, name='Добавление товара'),
    path('product/update/', views.product_update, name='Изменение данных о товаре'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)