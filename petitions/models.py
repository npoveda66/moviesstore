from django.db import models
from django.contrib.auth.models import User

    
class Petition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="petitions")
    created_at = models.DateTimeField(auto_now_add=True)

    # Want to make sure petitions actually implement vote model.
    def yes_votes(self):
        return self.votes.filter(vote_type="YES").count()
    
    def no_votes(self):
        return self.votes.filter(vote_type="NO").count() 
    
    def __str__(self):
        return self.title
    
class Vote(models.Model):
    VOTE_CHOICES = [
        ("YES", "Yes"),
        ("NO", "No"),
    ]

    petition = models.ForeignKey(Petition, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=3, choices=VOTE_CHOICES)

    class Meta:
        unique_together = ("petition", "user") # making sure users can't vote more than once.