from django.contrib import admin
from .models import Oficina


@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_corto')
    search_fields = ('nombre', 'nombre_corto')