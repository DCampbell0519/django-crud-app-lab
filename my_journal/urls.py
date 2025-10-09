from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('journal/', views.journal_index, name='journal-index')
]