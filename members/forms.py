from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['full_name', 'phone', 'gender', 'date_of_birth', 'address', 'profile_photo']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border-2 border-pink-200 focus:border-pink-500 focus:ring-4 focus:ring-pink-200 transition-all duration-200 bg-white/80 text-slate-800 placeholder-slate-400',
                'placeholder': 'Enter full name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border-2 border-pink-200 focus:border-pink-500 focus:ring-4 focus:ring-pink-200 transition-all duration-200 bg-white/80 text-slate-800 placeholder-slate-400',
                'placeholder': 'Enter phone number'
            }),
            'gender': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border-2 border-pink-200 focus:border-pink-500 focus:ring-4 focus:ring-pink-200 transition-all duration-200 bg-white/80 text-slate-800'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-3 rounded-lg border-2 border-pink-200 focus:border-pink-500 focus:ring-4 focus:ring-pink-200 transition-all duration-200 bg-white/80 text-slate-800'
            }),
            'address': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border-2 border-pink-200 focus:border-pink-500 focus:ring-4 focus:ring-pink-200 transition-all duration-200 bg-white/80 text-slate-800 placeholder-slate-400 resize-none',
                'rows': 4,
                'placeholder': 'Enter address'
            }),
            'profile_photo': forms.FileInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border-2 border-pink-200 focus:border-pink-500 focus:ring-4 focus:ring-pink-200 transition-all duration-200 bg-white/80 text-slate-800 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-gradient-to-r file:from-pink-500 file:to-rose-600 file:text-white file:font-semibold file:cursor-pointer hover:file:from-pink-600 hover:file:to-rose-700 file:transition-all file:duration-200'
            })
        }
        labels = {
            'full_name': 'Full Name',
            'phone': 'Phone Number',
            'gender': 'Gender',
            'date_of_birth': 'Date of Birth',
            'address': 'Address',
            'profile_photo': 'Profile Photo'
        }