from django.shortcuts import render, redirect
from WorldOfSpeedApp.profiles.models import Profile


def index(request):

    def get_profile():
        return Profile.objects.first()

    profile = get_profile()

    if profile:
        return render(request,"web/index.html",)
    return render(request, "web/index-no-profile.html",)
