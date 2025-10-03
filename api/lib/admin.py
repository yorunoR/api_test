from django.contrib import admin

from .models import Recipe

DEFAULT_READONLY_FIELDS = [
    "created_at",
    "updated_at",
]


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    readonly_fields = DEFAULT_READONLY_FIELDS
