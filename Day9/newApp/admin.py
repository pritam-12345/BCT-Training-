from django.contrib import admin
from .models import Product,productReview,Store,ProductCertificate

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'description','status')
    readonly_fields = ('created_at',)  # Make sure these fields exist in Product
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'products')
    


admin.site.register(Product, ProductAdmin)
admin.site.register(productReview)
admin.site.register(Store,StoreAdmin)
admin.site.register(ProductCertificate)

