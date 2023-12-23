from django.contrib import admin

from .models import Character


class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
    )


admin.site.register(Character)
