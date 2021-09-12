from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'mood_journal'

urlpatterns = [
    path('', views.home, name='home'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('mood/new/', views.mood_new, name='mood_new'),
    path('mood/<str:pk>/', views.mood_edit, name='post_edit'),
]