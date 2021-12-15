from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'price', 'created_at', 'updated_at')
