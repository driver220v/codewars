from django.urls import path
from .views import task, home

urlpatterns = [
    path('', home),
    path('task/', task)
]