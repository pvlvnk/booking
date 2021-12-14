from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'role',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
    )
    list_filter = ('role',)
    list_editable = ('role',)
    empty_value_display = '-empty-'


admin.site.register(User, UserAdmin)
