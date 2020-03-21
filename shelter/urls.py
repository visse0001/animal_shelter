from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_animal/', views.add_animal, name='add-animal'),
    path('register/', views.register, name='register'),
]
