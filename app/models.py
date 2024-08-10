from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Price(models.Model):
    date = models.DateField(auto_now_add=True)
    price_per_liter = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.price_per_liter} on {self.date}'

class MilkPurchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.DecimalField(max_digits=5, decimal_places=2)  # Liters
    price_per_liter = models.ForeignKey(Price, on_delete=models.CASCADE)

    def total_price(self):
        return self.quantity * self.price_per_liter.price_per_liter

    def __str__(self):
        return f'{self.customer.user.username} - {self.date}'
