from django.urls import path
from . import views

urlpatterns = [
    # Jab URL khali ho (''), toh views.home function call karo
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects_page, name='projects'),
]