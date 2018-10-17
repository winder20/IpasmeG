from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import Account

# Register your models here.
# admin.site.register(Account)

@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('cedula', 'nombre','apellido','fecha_naci','email','is_staff')
    list_filter = ('cedula','nombre','apellido','fecha_naci','email','is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('cedula', 'naciona',)
    ordering = ('cedula',)
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {'fields': ('cedula', 'password')  }),
        (_('Personal info'), {'fields': ('cedula','nombre','apellido','fecha_naci','email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cedula','nombre','apellido','fecha_naci','email','password1', 'password2'),
        }),
    )