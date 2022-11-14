from django.shortcuts import render
from django.contrib import messages
from Tracking.Tracking import TrackTrack
# Create your views here.

def tracking(request):
    track = TrackTrack(request.POST or None)
    if track.is_valid():
        track.save()
        messages.success(request, 'Volando')
        track = TrackTrack()
    else:
        messages.error(request, 'No creo')
    context = {'track': track}
    return render(request, 'tracking.html', context)

