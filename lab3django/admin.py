from django.utils.html import format_html
from lab3django.models import Pokupatel, Tovar, Korzina, Tovar_M
from django.contrib import admin

# Register your models here.
admin.site.register(Pokupatel)
admin.site.register(Tovar)


class TovarMInline(admin.TabularInline):
    model = Tovar_M
    fields = ("tovar", "count")


@admin.register(Korzina)
class KorzinaAdmin(admin.ModelAdmin):
    list_display = ("id", "pokupatel", "tovar_count", "total_price", "status")
    list_filter = ("pokupatel__name", "tovar__name")
    search_fields = ("pokupatel__name", "tovar__name")
    readonly_fields = ("tovar_count", "total_price")

    inlines = (TovarMInline,)
    date_hierarchy = "created_at"

    def status(self, obj):
        if obj.is_buyed:
            return format_html("<span style='color: green';>Выкуплена</span>")
        else:
            return format_html("<span style='color: red';>Не выкуплена</span>")
