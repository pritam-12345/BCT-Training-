from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'description','status')
    readonly_fields = ('created_at',)  # Make sure these fields exist in Product

admin.site.register(Product, ProductAdmin)

