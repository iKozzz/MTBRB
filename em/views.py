from django.shortcuts import render, redirect
from django.views import generic

from em.forms import *
from .models import *


class RidersView(generic.ListView):
    template_name = 'riders.html'
    context_object_name = 'riders_list'

    def get_queryset(self):
        return Rider.objects.order_by('id')[:]


class RiderDetailsView(generic.DetailView):
    model = Rider
    template_name = 'rider_details.html'


class StagesView(generic.ListView):
    template_name = 'stages.html'
    context_object_name = 'stages_list'

    def get_queryset(self):
        return Stage.objects.order_by('date_start')[:]


class StageDetailsView(generic.DetailView):
    model = Stage
    template_name = 'stage_details.html'


class LiderboardView(generic.ListView):
    model = Rider
    template_name = 'liderboard.html'

    def get_queryset(self):
        return Rider.objects.order_by('created_at')[:]


def rider_add(request):
    if request.method == 'POST':
        form = RiderAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('em:riders')
    else:
        form = RiderAddForm()
    return render(request, 'rider_add_form.html', {
        'form': form
    })


def stage_add(request):
    if request.method == 'POST':
        form = StageAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('em:stages')
    else:
        form = StageAddForm()
    return render(request, 'stage_add_form.html', {
        'form': form
    })
