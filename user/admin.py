from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone_number','slug')
    list_display_links=('phone_number',)
    list_editable=('last_name',)
    search_fields=('first_name','last_name','email')
    readonly_fields=('slug',)
    list_filter=('email',)
    list_per_page=10


admin.site.register(models.UserProfile)
admin.site.register(models.Post)