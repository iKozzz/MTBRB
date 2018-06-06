from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Rider


class IndexView(generic.ListView):
    template_name = 'em/index.html'
    context_object_name = 'riders_list'

    def get_queryset(self):
        return Rider.objects.order_by('rider_name')[:]


class RiderDetailsView(generic.DetailView):
    model = Rider
    template_name = 'em/rider_details.html'


class ResultsView(generic.DetailView):
    model = Rider
    template_name = 'em/results.html'


def results(request, rider_id):
    rider = get_object_or_404(Rider, pk=rider_id)
    return render(request, 'em/results.html', {'rider': rider})


def rider_add(request):
    r = Rider(rider_name=request.POST['rider_name'], rider_bike=request.POST['rider_bike'])
    r.save()
    return HttpResponseRedirect(reverse('em:index'))
