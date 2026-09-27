# ministries/admin.py

from django.contrib import admin
from .models import Ministry, MembershipRequest

@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MembershipRequest)
class MembershipRequestAdmin(admin.ModelAdmin):
    list_display = ('ministry', 'user', 'approved', 'created_at')
    list_filter = ('approved', 'ministry')
    search_fields = ('user__username', 'ministry__name')

# TEST: visit /admin/ -> Ministries section visible


#register your models here.
