from django.urls import path
from . import views

urlpatterns = [
  path('store/',views.saludo),
]