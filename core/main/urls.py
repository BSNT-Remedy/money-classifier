from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path("register/", views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="main/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="main:index"), name="logout"),
    path('analytics/', views.analytics, name='analytics'),
    path('save_prediction/', views.save_prediction, name='save_prediction'),
    path('api/predictions_stats/', views.predictions_stats, name='predictions_stats'),
    path("about/", views.model_card, name="about"),
    path("ethics/", views.ethics_statement, name="ethics"),
]
