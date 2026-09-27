# ministries/forms.py

from django import forms
from .models import Ministry, MembershipRequest

class MinistryForm(forms.ModelForm):
    class Meta:
        model = Ministry
        fields = ['name', 'slug', 'description', 'leader', 'members']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

# Simple join/request form for members
class JoinRequestForm(forms.ModelForm):
    class Meta:
        model = MembershipRequest
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Why do you want to join? (optional)'}),
        }

# TEST: forms importable; admin will use MinistryForm if needed
