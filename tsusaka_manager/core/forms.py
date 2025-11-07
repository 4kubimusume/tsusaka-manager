from django import forms
from .models import Participant, Match

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'type']

class MatchForm(forms.ModelForm):
    score_player1 = forms.CharField(required=True)
    score_player2 = forms.CharField(required=True)
    winner = forms.ModelChoiceField(queryset=Participant.objects.all(), required=True)

    class Meta:
        model = Match
        fields = ['player1', 'player2', 'table_number', 'score_player1', 'score_player2', 'winner']

    def clean(self):
        cleaned_data = super().clean()
        score1 = cleaned_data.get("score_player1")
        score2 = cleaned_data.get("score_player2")
        winner = cleaned_data.get("winner")

        if not score1 or not score2 or not winner:
            raise forms.ValidationError("スコアと勝者をすべて入力してください。")

        return cleaned_data

class MatchScoreForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['score_player1', 'score_player2', 'winner']
