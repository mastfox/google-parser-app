from django.urls import path
from django.views.generic import TemplateView
from homepage import views
from homepage.views import AboutView, ContactView


urlpatterns = [
    path('', views.index_view),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view())
]
