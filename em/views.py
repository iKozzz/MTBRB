from django.shortcuts import render, redirect
from django.views import generic

from em.forms import *
from .models import *


class RidersView(generic.ListView):
    template_name = 'riders.html'
    context_object_name = 'data'

    def get_queryset(self):
        riders = Rider.objects.order_by('id')[:]
        stages = Stage.objects.order_by('date_start')[:]
        return {'riders': riders, 'stages': stages};


class RiderDetailsView(generic.DetailView):
    model = Rider
    template_name = 'rider_details.html'


class StagesView(generic.ListView):
    template_name = 'stages.html'
    context_object_name = 'stages_list'

    def get_queryset(self):
        return Stage.objects.order_by('date_start')[:]


def StageDetailsView(request, pk):
    stage = Stage.objects.get(id = pk)
    riders_in_stage = Riders_And_Stage.objects.filter(stage = stage)
    riders = []
    for rider_in_stage in riders_in_stage:
        print(rider_in_stage.rider)

        rider = Rider.objects.get(id=rider_in_stage.rider.id)
        
        riders.append({
            'id': rider.id,
            'name': rider.name,
            'photo': rider.photo
        })

    return render(request, 'stage_details.html', {'riders': riders, 'stage': stage})


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

def rider_stage_assign(request, rider_id, stage_id):
    rider = Rider.objects.get(id = rider_id)
    stage = Stage.objects.get(id = stage_id)
    if (Riders_And_Stage.objects.filter(rider = rider, stage = stage) is None):
        print('tst')
        Riders_And_Stage(rider = rider, stage = stage).save()
    return redirect('em:riders')


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
