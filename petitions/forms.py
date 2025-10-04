from django import forms
from .models import Petition, Vote

class PetitionForm(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ["title", "description"]

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ["vote_type"]