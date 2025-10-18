from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('journal/', views.journal_index, name='journal-index'),
    path('journal/<int:journal_id>/', views.journal_detail, name='journal-detail'),
    # Class Based Views below
    path('journal/create/', views.JournalCreate.as_view(), name='journal-create'),
    path('journal/<int:pk>/update/', views.JournalUpdate.as_view(), name='journal-update'),
    path('journal/<int:pk>/delete/', views.JournalDelete.as_view(), name='journal-delete'),
    path('journal/<int:journal_id>/add-thought/', views.add_thought, name='add-thought'),
    # path('thought/<int:pk>/update/', views.ThoughtUpdate.as_view(), name='thought-update'),
    # path('thought/<int:pk>/delete/', views.ThoughtDelete.as_view(), name='thought-delete'),
]