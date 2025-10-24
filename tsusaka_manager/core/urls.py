from django.urls import path
from . import views

urlpatterns = [
    path("participants/", views.participant_list, name="participant_list"),
    path('add/', views.participant_create, name='participant_create'),
    path('edit/<int:participant_id>/', views.participant_edit, name='participant_edit'),
]
