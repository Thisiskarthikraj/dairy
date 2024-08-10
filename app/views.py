from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MilkPurchase, Customer
from django.db.models import Sum

@login_required


def view_purchases(request):
    purchases = MilkPurchase.objects.select_related('price_per_liter').all()
    total_amount = sum(purchase.total_price() for purchase in purchases)  # Calculate total amount
    return render(request, 'view_purchases.html', {'purchases': purchases, 'total_amount': total_amount})


def home(request):
    return render(request, 'index.html')


