from django.shortcuts import redirect, render, get_object_or_404
from django.forms import modelform_factory
from .models import Meeting, Room
from .form import MeetingForm
# Create your views here.


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)

    return render(request, 'meetings/detail.html', {'meeting': meeting})


def room_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms": Room.objects.all()})


# MeetingForm = modelform_factory(Meeting, exclude=[])


def form(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = MeetingForm()

    return render(request, "meetings/form.html", {"form": form})
