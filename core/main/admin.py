from django.contrib import admin
from .models import Prediction

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('label', 'confidence', 'user', 'created_at')
    list_filter = ('label', 'created_at')
    search_fields = ('label',)
