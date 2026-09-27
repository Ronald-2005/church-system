from django import forms
from .models import Contribution

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = [
            'giver',
            'amount',
            'payment_method',
            'mpesa_transaction_code',
            'mpesa_phone_number',
            'mpesa_status',
            'notes',
        ]
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        payment_method = cleaned_data.get('payment_method')

        # Ensure M-Pesa details are filled when payment method is M-Pesa
        if payment_method == 'M-Pesa':
            if not cleaned_data.get('mpesa_transaction_code'):
                self.add_error('mpesa_transaction_code', 'Transaction code is required for M-Pesa payments.')
        return cleaned_data
