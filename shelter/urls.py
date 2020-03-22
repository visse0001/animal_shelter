from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_animal/', views.add_animal, name='add-animal'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='shelter/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='shelter/logout.html'), name='logout'),
    path('update_animal/<str:id>/', views.update_animal, name='update-animal'),
    path('delete_animal/<str:id>/', views.delete_animal, name='delete-animal'),
    path('animals_for_adoption/', views.animals_for_adoption, name='animal-for-adoption'),
]
