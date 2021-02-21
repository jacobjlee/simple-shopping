from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models
from products.models import Product
from orders.models import Order, OrderStatus, OrderItem


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': (
            'name', 'phone_number', 'address', 'gender'
        )}),
        
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : (
                'email', 'password1', 'password2', 'name', 'phone_number', 'address', 'gender'
            )
        }),
    )
    
admin.site.register(models.User, UserAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(OrderItem)
