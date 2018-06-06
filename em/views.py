from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from em.forms import RiderAddForm
from .models import Rider


class IndexView(generic.ListView):
    template_name = 'em/index.html'
    context_object_name = 'riders_list'

    def get_queryset(self):
        return Rider.objects.order_by('name')[:]


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
    if request.method == 'POST':
        form = RiderAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('em:index')
    else:
        form = RiderAddForm()
    return render(request, 'em/rider_add_form.html', {
        'form': form
    })
