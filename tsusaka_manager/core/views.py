from django.shortcuts import render, redirect, get_object_or_404
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

def participant_edit(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'participants/form.html', {'form': form})