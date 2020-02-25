from django.urls import path
from django.views.generic import TemplateView
from jboard import views


urlpatterns = [
    path('jboard/', views.jboard_view),
    path('create/', views.create),
    path('delete/', views.delete),
    path('export/csv/', views.export_data_csv, name='export_data_csv')
]
