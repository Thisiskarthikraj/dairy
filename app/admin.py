from django.contrib import admin
from .models import MilkPurchase, Customer, Price

# Register your models here.


class MilkPurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date', 'quantity', 'price_per_liter')  # Customize as needed
    search_fields = ('customer__user__username', 'date')

admin.site.register(MilkPurchase, MilkPurchaseAdmin)
admin.site.register(Customer)
admin.site.register(Price)
