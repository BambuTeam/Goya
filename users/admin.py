# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
# models
from django.contrib.auth.models import User
from users.models import Profile
"""
registro bagre
admin.site.register(Profile)
abajo se usa el decorador para registrarlo en una linea
"""
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """profile admin """
    list_display = ('pk', 'user', 'phone_number', 'picture')
    list_display_links = ('pk','user', 'phone_number')
    list_editable = ('picture',)
    """campos de busqueda de la administracio """
    search_fields = (
        'user__email',
        'user_first_name',
        'user__last_name',
        'phone_number')
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff')
    fieldsets = (
        ('Profile', {
            'fields':(('user', 'picture'),),
        }),
        ('Extra Info', {
            'fields':(
                ('phone_number'),
                ('biograpy'),),
        }),
        ('Metadata', {
            'fields':(('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified',)

class ProfileInline(admin.StackedInline):
    """profile in line admin for users"""
    model = Profile
    can_delete= False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """add profile admin to base user admin"""
    inlines = (ProfileInline,)
    list_display=(
        'username',
        'email',
        'first_name',
        'is_active',
        'is_staff'

    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
