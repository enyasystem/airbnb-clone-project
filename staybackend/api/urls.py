from django.urls import path

from staybackend.api.views import health

urlpatterns = [
    path('health/', health, name='health'),
]
