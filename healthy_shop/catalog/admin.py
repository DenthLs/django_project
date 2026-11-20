from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('title',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone', 'product', 'quantity', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('customer_name', 'phone')