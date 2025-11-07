from django.urls import path
from . import views

urlpatterns = [
    path("participants/", views.participant_list, name="participant_list"),
    path('add/', views.participant_create, name='participant_create'),
    path('edit/<int:participant_id>/', views.participant_edit, name='participant_edit'),
    path('delete/<int:participant_id>/', views.participant_delete, name='participant_delete'),
    path('matches/', views.match_list, name='match_list'),
    path('matches/add/', views.match_create, name='match_create'),
    path('matches/edit/<int:match_id>/', views.match_edit, name='match_edit'),
]
