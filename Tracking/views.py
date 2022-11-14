from django.shortcuts import render
from django.contrib import messages
from Tracking.Tracking import TrackTrack
from Tracking.site import SiteSite

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

def Site(request):
    site = SiteSite(request.POST or None)
    if site.is_valid():
        site.save()
        messages.success(request, 'Acachete')
        site = SiteSite()
    else:
        messages.error(request, 'Muy mal')
    context = {'site': site}
    return render(request, 'site.html', context)
