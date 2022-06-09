from django.contrib import admin
from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    ordering = ("-name",)
    search_fields = ("name",)
    list_editable = ("name",)
    list_per_page = 3
    

admin.site.register(City, CityAdmin)