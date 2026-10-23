from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]