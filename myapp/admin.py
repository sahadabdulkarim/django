from django.contrib import admin
from .models import DummyModel


class DummyModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


admin.site.register(DummyModel, DummyModelAdmin)
