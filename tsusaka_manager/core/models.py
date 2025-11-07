from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class MatchProgress(models.Model):
    participant1 = models.ForeignKey(Participant, related_name='match_as_p1', on_delete=models.CASCADE)
    participant2 = models.ForeignKey(Participant, related_name='match_as_p2', on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    table_number = models.IntegerField()

    def __str__(self):
        return f"Match {self.id}: {self.participant1} vs {self.participant2}"


class MatchResult(models.Model):
    match = models.OneToOneField(MatchProgress, on_delete=models.CASCADE)
    winner = models.ForeignKey(Participant, on_delete=models.CASCADE)
    # 最小限なのでスコアはセット単位管理はせず、あとで拡張
    score_p1 = models.IntegerField()
    score_p2 = models.IntegerField()

    def __str__(self):
        return f"Result of Match {self.match.id}"


class MatchRequest(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    queue_number = models.IntegerField()

    class Meta:
        unique_together = ('participant', 'queue_number')

    def __str__(self):
        return f"Request: {self.participant.name} ({self.queue_number})"

class Match(models.Model):
    id = models.AutoField(primary_key=True)
    player1 = models.ForeignKey(Participant, related_name='matches_as_player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Participant, related_name='matches_as_player2', on_delete=models.CASCADE)
    table_number = models.IntegerField(null=True, blank=True)
    score_player1 = models.CharField(max_length=20)  # 例: "11-8, 8-11, 11-9"
    score_player2 = models.CharField(max_length=20)
    winner = models.ForeignKey(Participant, related_name='wins', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.player1.name} vs {self.player2.name}"
