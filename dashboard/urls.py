from django.urls import path
from django.views.generic import TemplateView
from dashboard import views


urlpatterns = [
    path('dashboard/', views.dashboard_view)
]
