from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
from django.views import generic
from django.views.generic.list import ListView
from Tracking.Tracking import TrackTrack
from Tracking.models import TrackDocument
from Tracking.site import SiteSite
# Create your views here.
class document_list(ListView):
    model = TrackDocument
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
def index(request):
    return render(request, "Tracking/index.html")
def tracking(request):
    track = TrackTrack(request.POST or None)
    if track.is_valid():
        track.save()
        messages.success(request, 'Confirmado')
        track = TrackTrack()
    else:
        messages.error(request, 'Error')
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
