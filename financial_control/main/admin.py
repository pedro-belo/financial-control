from django.contrib import admin
from .models import Record, RecordEntry

# Register your models here.
@admin.register(Record)
class RecordModel(admin.ModelAdmin):
    list_display = "name", "parent", "user", "created_at"


@admin.register(RecordEntry)
class RecordEntryModel(admin.ModelAdmin):
    list_display = "name", "year", "parent", "created_at"
