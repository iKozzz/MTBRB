from datetime import datetime

from django.shortcuts import render, redirect
from django.views import generic

from em.controllers.race_controller import *
from em.forms import *
from .models import *


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class RidersView(generic.ListView):
    template_name = 'riders.html'
    context_object_name = 'data'

    def get_queryset(self):
        riders = Rider.objects.order_by('id')[:]
        stage = None
        if Stage.objects.exists():
            stage = Stage.objects.order_by('date_start').filter(date_start__gte=datetime.now())[:1].get()
        return {'riders': riders, 'stage': stage}


class RiderDetailsView(generic.DetailView):
    model = Rider
    template_name = 'rider_details.html'


class StagesView(generic.ListView):
    template_name = 'stages.html'
    context_object_name = 'stages_list'

    def get_queryset(self):
        return Stage.objects.order_by('date_start')[:]


def stage_details(request, pk):
    stage = Stage.objects.get(id=pk)
    riders_in_stage = RiderAndStage.objects.filter(stage=stage)
    riders = []
    for rider_in_stage in riders_in_stage:
        rider = Rider.objects.get(id=rider_in_stage.rider.id)
        riders.append({
            'id': rider.id,
            'name': rider.name,
            'photo': rider.photo
        })
    return render(request, 'stage_details.html', {'riders': riders, 'stage': stage})


class RacesView(generic.ListView):
    template_name = 'races.html'
    context_object_name = 'data'

    def get_queryset(self):
        races = Race.objects.order_by('id')[:]
        stage = Stage.objects.order_by('date_start').filter(date_start__gte=datetime.now())[:1].get()
        return {'races': races, 'stage': stage}


def race_details(request, pk):
    race = Race.objects.get(id=pk)
    # races_in_stage = RiderStageRace.objects.filter(race=race)
    # races = []
    # for race_in_stage in races_in_stage:
    #     race = Race.objects.get(id=race_in_stage.race.id)
    #     races.append({
    #         'id': race.id,
    #         'name': race.name
    #     })
    return render(request, 'race_details.html', {'race': race, 'stage': None})


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
    rider = Rider.objects.get(id=rider_id)
    stage = Stage.objects.get(id=stage_id)
    if RiderAndStage.objects.filter(rider=rider, stage=stage).count() == 0:
        RiderAndStage(rider=rider, stage=stage).save()
    return redirect('em:riders')


def rider_stage_unassign(request, rider_id, stage_id):
    rider = Rider.objects.get(id=rider_id)
    stage = Stage.objects.get(id=stage_id)
    RiderAndStage.objects.get(rider=rider, stage=stage).delete()
    return redirect('em:stage_details', stage_id)


def rider_race_assign(request, rider_id, stage_id, race_id):
    rider = Rider.objects.get(id=rider_id)
    stage = Stage.objects.get(id=stage_id)
    race = Race.objects.get(id=race_id)
    if RiderStageRace.objects.filter(rider=rider, stage=stage, race=race).count() == 0:
        RiderStageRace(rider=rider, stage=stage, race=race).save()
    return redirect('em:races')


def rider_race_unassign(request, rider_id, stage_id, race_id):
    rider = Rider.objects.get(id=rider_id)
    stage = Stage.objects.get(id=stage_id)
    race = Race.objects.get(id=race_id)
    RiderStageRace.objects.get(rider=rider, stage=stage, race=race).delete()
    return redirect('em:race_details', race_id)


def rider_delete(request, rider_id):
    rider = Rider.objects.get(id=rider_id)
    Rider.objects.get(id=rider.id).delete()
    return redirect('em:riders')


def stage_delete(request, stage_id):
    stage = Stage.objects.get(id=stage_id)
    Stage.objects.get(id=stage.id).delete()
    return redirect('em:stages')


def race_delete(request, race_id):
    race = Race.objects.get(id=race_id)
    Race.objects.get(id=race.id).delete()
    return redirect('em:stages')


def rider_prepare_to_race(request, rider_id):
    set_rider_ready(rider_id)
    return redirect('em:rider_details', rider_id)


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


def race_add(request):
    if request.method == 'POST':
        form = RaceAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('em:races')
    else:
        form = RaceAddForm()
    return render(request, 'race_add_form.html', {
        'form': form
    })
