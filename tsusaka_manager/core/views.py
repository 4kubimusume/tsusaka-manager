from django.shortcuts import render, redirect
from .models import Participant
from .forms import ParticipantForm

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, "participants/list.html", {"participants": participants})

def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'participants/form.html', {'form': form})