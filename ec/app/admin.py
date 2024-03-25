from django.contrib import admin
from .models import Product, Customer, Cart, OrderPlaced, Supplier,Category

@admin.register(Supplier)
class SupplierModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_number', 'email', 'address']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'category', 'description', 'product_image', 'get_supplier_name']

    def get_supplier_name(self, obj):
        return obj.supplier.name if obj.supplier else ''
    get_supplier_name.short_description = 'Supplier'

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'order_date', 'status', 'payment']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']