from django.urls import path
from .views import apiOverview

urlpatterns = [
    path('', apiOverview),
]