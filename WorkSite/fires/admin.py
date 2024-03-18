from django.contrib import admin

from fires.models import Fire


# Register your models here.
@admin.register(Fire)
class FireAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'message_from')