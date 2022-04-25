from django.shortcuts import render
from django.views.generic import ListView

from app.models import Profile


class MainPageView(ListView):
    model = Profile
    template_name = 'index.html'
    context_object_name = 'profile'

