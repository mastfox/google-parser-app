from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.index_view),
    # path('index', views.index_view),
]
