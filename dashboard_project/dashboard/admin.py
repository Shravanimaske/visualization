from django.contrib import admin
from .models import DataPoint

class DataPointAdmin(admin.ModelAdmin):
    list_display = ('year', 'country', 'topics', 'intensity', 'likelihood', 'relevance', 'region', 'city')
    list_filter = ('year', 'country', 'topics', 'region')
    search_fields = ('year', 'country', 'topics', 'region', 'city')

admin.site.register(DataPoint, DataPointAdmin)
