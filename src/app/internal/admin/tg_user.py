from django.contrib import admin
from app.internal.models.tg_user import tgUser


@admin.register(tgUser)
class AdminTgUser(admin.ModelAdmin):
    list_display = ('username', 'phone_number')
