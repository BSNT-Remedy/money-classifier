from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('analytics/', views.analytics, name='analytics'),
    path('save_prediction/', views.save_prediction, name='save_prediction'),
    path('api/predictions_stats/', views.predictions_stats, name='predictions_stats'),
]
