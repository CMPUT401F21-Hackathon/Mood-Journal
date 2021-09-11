from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'mood_journal'

urlpatterns = [
    path('', views.home, name='home'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]