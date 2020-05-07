from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_Recipe, name='get_Recipe'),
]