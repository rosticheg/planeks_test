from django.contrib import admin
from csv_gen.models import Schema

class SchemaAdmin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(Schema, SchemaAdmin)

