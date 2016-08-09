from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import User


class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'is_staff', 'is_active')
    list_display_links = ('email', )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', )
    ordering = ('id', 'email', )
    filter_horizontal = ('groups', 'user_permissions',)


# Register your models here.
admin.site.register(User, CustomUserAdmin)
