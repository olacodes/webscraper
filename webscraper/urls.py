
from django.urls import path, include
from .views import WebScraperView


urlpatterns = [
    path('', WebScraperView.as_view())
]
