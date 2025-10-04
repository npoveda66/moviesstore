from django.urls import path
from . import views

urlpatterns = [
    path("", views.petition_list, name="petitions.petition_list"),
    path("new/", views.petition_create, name="petitions.petition_create"),
    path("<int:id>", views.petition_detail, name="petitions.petition_detail"),
]