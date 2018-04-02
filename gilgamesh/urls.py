"""Defines url patterns for gilgamesh."""

from django.urls import path

from . import views

app_name = 'gilgamesh'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    #pagania Sobre
    path('about/', views.about, name='about'),

    #pagina de downloads
    path('download/', views.download, name='download'),

]