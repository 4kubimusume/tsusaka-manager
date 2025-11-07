from django.shortcuts import render, redirect, get_object_or_404
from .models import Participant, Match
from .forms import ParticipantForm, MatchForm, MatchScoreForm

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

def participant_delete(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    if request.method == 'POST':
        participant.delete()
        return redirect('participant_list')
    return render(request, 'participants/confirm_delete.html', {'participant': participant})

def match_list(request):
    matches = Match.objects.all().select_related('player1', 'player2')
    return render(request, 'matches/list.html', {'matches': matches})

def match_create(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('match_list')
    else:
        form = MatchForm()
    return render(request, 'matches/form.html', {'form': form})

def match_edit(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    if request.method == 'POST':
        form = MatchScoreForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('match_list')
    else:
        form = MatchScoreForm(instance=match)
    return render(request, 'matches/edit.html', {'form': form, 'match': match})
