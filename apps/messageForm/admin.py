from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.messageForm.models import MessageUser


class MessageUserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(MessageUser, MessageUserProfileAdmin)
