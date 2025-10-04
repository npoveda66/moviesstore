from django.contrib import admin
from .models import Petition, Vote

# Register your models here.
class PetitionAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_at", "yes_votes", "no_votes")
    search_fields = ("title", "description", "created_by__username")
    list_filter = ("created_at",)

class VoteAdmin(admin.ModelAdmin):
    list_display = ("petition", "user", "vote_type")
    list_filter = ("vote_type",)
    search_fields = ("petition__title", "user__username")

admin.site.register(Petition, PetitionAdmin)
admin.site.register(Vote, VoteAdmin)