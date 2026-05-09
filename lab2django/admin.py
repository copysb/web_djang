from lab2django.models import Pokupatel, Tovar, Korzina
from django.contrib import admin

# Register your models here.
admin.site.register(Pokupatel)
admin.site.register(Tovar)


@admin.register(Korzina)
class KorzinaAdmin(admin.ModelAdmin):
    list_display = ("id", "pokupatel", "tovar_count")
    list_filter = ("pokupatel__name", "tovar__name")
    search_fields = ("pokupatel__name", "tovar__name")
