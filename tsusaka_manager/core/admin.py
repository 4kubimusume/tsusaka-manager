from django.contrib import admin
from .models import Participant, MatchProgress, MatchResult, MatchRequest

admin.site.register(Participant)
admin.site.register(MatchProgress)
admin.site.register(MatchResult)
admin.site.register(MatchRequest)
