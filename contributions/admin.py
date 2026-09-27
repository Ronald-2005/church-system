from django.contrib import admin
from .models import Contribution

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('id', 'giver_name', 'amount', 'payment_method', 'mpesa_transaction_code', 'date')
    list_filter = ('payment_method', 'date')
    search_fields = ('giver__username', 'mpesa_transaction_code', 'mpesa_phone_number', 'household__name')
    date_hierarchy = 'date'

    def giver_name(self, obj):
        return obj.giver.username if obj.giver else "Anonymous"
    giver_name.short_description = "Giver"


# Register your models here.
