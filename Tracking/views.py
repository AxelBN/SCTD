from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from django.views.generic import UpdateView, DeleteView
from django.views.generic.list import ListView
from Tracking.Tracking import TrackTrack
from Tracking.models import TrackDocument
from Tracking.site import SiteSite
from django.contrib.messages.views import SuccessMessageMixin
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
    return render(request, 'Tracking/tracking.html', context)

def Site(request):
    site = SiteSite(request.POST or None)
    if site.is_valid():
        site.save()
        messages.success(request, 'Acachete')
        site = SiteSite()
    else:
        messages.error(request, 'Muy mal')
    context = {'site': site}
    return render(request, 'Tracking/site.html', context)

class update_document(UpdateView, SuccessMessageMixin):
    model = TrackDocument
    fields = "__all__"
    template_name = 'Tracking/update_documents.html'
    success_message = 'Cliente actualizado'
    def updt_document(self):
        return reverse('documents')

def delete_document(request, pk):
    document = get_object_or_404(TrackDocument, id=pk)
    document.delete()

    return redirect('/tracking_list.html')

