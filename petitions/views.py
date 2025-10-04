from django.shortcuts import render, redirect, get_object_or_404
from .models import Petition, Vote
from django.contrib.auth.decorators import login_required
from .forms import PetitionForm, VoteForm

# Create your views here.

@login_required
def petition_list(request):
    petitions = Petition.objects.all().order_by("-created_at")
    return render(request, "petitions/petition_list.html", {"petitions": petitions})

@login_required
def petition_create(request):
    if request.method == "POST":
        form = PetitionForm(request.POST)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.created_by = request.user
            petition.save()
            return redirect("..")
    else:
        form = PetitionForm()
    return render(request, "petitions/petition_form.html", {"form": form})

@login_required
def petition_detail(request, id):
    petition = get_object_or_404(Petition, id=id)
    existing_vote = Vote.objects.filter(petition=petition, user=request.user).first()

    if request.method == "POST" and not existing_vote:
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.petition = petition
            vote.user = request.user
            vote.save()
            return redirect(".", id=petition.id)
    else:
        form = VoteForm()

    return render(
        request, 
        "petitions/petition_detail.html",
        {
            "petition": petition,
            "form": form,
            "existing_vote": existing_vote,
        }
    )