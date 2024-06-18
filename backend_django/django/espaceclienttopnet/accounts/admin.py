from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'cin', 'name',  'is_staff', 'is_active')
    list_filter = ('is_admin', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'cin', 'name', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'cin', 'name', 'password1', 'password2', 'is_admin', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'cin', 'name')
    ordering = ('email',)

    # Remove filter_horizontal or adjust it accordingly
    filter_horizontal = ()
    list_filter = ()

admin.site.register(CustomUser, CustomUserAdmin)
