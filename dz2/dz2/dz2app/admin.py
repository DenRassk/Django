from django.contrib import admin
from .models import User, Product, Order

# Register your models here.
# ДЗ к семинару № 5


@admin.action(description="Сбросить количество в ноль")
def quantity_reset(modeladmin, request, queryset):
    queryset.update(quantity=0)


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по Имени пользователя'
    fields = ['name', 'email', 'tel', 'address', 'date_reg']
    readonly_fields = ['date_reg']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['name']
    list_filter = ['price', 'quantity']
    search_fields = ['name']
    search_help_text = 'Поиск по Наименованию товара'
    actions = [quantity_reset]
    fields = ['name', 'description', 'date_reg', 'price', 'quantity', 'image']
    readonly_fields = ['date_reg']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['date_ordered', 'total_price']
    ordering = ['date_ordered']
    list_filter = ['date_ordered']
    fields = ['date_ordered', 'customer', 'products', 'total_price']
    readonly_fields = ['date_ordered']


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
