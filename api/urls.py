from django.urls import path
from .views import apiOverview, getAllProducts

urlpatterns = [
    path('', apiOverview),
    path('api/products/', getAllProducts),
]