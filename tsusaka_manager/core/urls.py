from django.urls import path
from . import views

urlpatterns = [
    path("participants/", views.participant_list, name="participant_list"),
]
