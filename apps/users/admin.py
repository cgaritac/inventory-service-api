from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('role', 'company')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'company')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('role', 'company')}),
    )
