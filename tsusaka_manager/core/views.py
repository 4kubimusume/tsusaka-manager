from django.shortcuts import render
from .models import Participant

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, "participants/list.html", {"participants": participants})
