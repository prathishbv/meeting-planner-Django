from django.shortcuts import render
from meetings.models import Meeting

def welcome(request):
    return render(request, 'website/home.html', {'meetings': Meeting.objects.all()})
