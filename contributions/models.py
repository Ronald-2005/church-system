from django.db import models
from members.models import Member

class Contribution(models.Model):
    PAYMENT_METHODS = [
        ('Cash', 'Cash'),
        ('M-Pesa', 'M-Pesa'),
        ('Bank', 'Bank Transfer'),
        ('Cheque', 'Cheque'),
        ('Other', 'Other'),
    ]

    giver = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='contributions'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='Cash')
    date = models.DateTimeField(auto_now_add=True)

    # Optional M-Pesa details
    mpesa_transaction_code = models.CharField(max_length=64, blank=True, null=True)
    mpesa_phone_number = models.CharField(max_length=20, blank=True, null=True)
    mpesa_status = models.CharField(max_length=30, blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.giver.full_name} - {self.amount} ({self.payment_method})"
