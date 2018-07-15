import os

from django.db.models import Sum, Min, Max, Count
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
        riders_in_stage = []
        if Stage.objects.exists():
            if Stage.objects.order_by('date_start').filter(date_start__gte=datetime.now()-timedelta(days=3)).exists():
                stage = Stage.objects.order_by('date_start').filter(
                    date_start__gte=datetime.now()-timedelta(days=3)
                )[:1].get()
                riders_in_stage_table = RiderAndStage.objects.filter(stage=stage)
                for rider_in_stage_table in riders_in_stage_table:
                    rider = Rider.objects.get(id=rider_in_stage_table.rider.id)
                    riders_in_stage.append({
                        'number': rider.number,
                        'id': rider.id,
                        'name': rider.name
                    })
        return {'riders': riders, 'stage': stage, 'riders_in_stage': riders_in_stage}


class RiderDetailsView(generic.DetailView):
    model = Rider
    template_name = 'rider_details.html'


class StagesView(generic.ListView):
    template_name = 'stages.html'
    context_object_name = 'stages_list'

    def get_queryset(self):
        return Stage.objects.order_by('date_start')[:]


class LiderboardView(generic.ListView):
    template_name = 'liderboard.html'
    context_object_name = 'data'

    def get_queryset(self):
        riders = Rider.objects.order_by('id')[:]
        stage = None
        results = None
        stage_leaders = None
        if Stage.objects.exists():
            if Stage.objects.order_by('date_start').filter(date_start__gte=datetime.now() - timedelta(days=3)).exists():
                stage = Stage.objects.order_by('date_start').filter(
                    date_start__gte=datetime.now() - timedelta(days=3)
                )[:1].get()
                stage_leaders = get_leaders_for_stage(stage)
        return {
            'riders': riders,
            'stage': stage,
            'results': results,
            'stage_leaders': stage_leaders,
        }


def stage_details(request, pk):
    stage = Stage.objects.get(id=pk)
    tracks = Track.objects.filter(stage_id=pk)
    riders_in_stage = RiderAndStage.objects.filter(stage=stage)
    riders = []
    for rider_in_stage in riders_in_stage:
        rider = Rider.objects.get(id=rider_in_stage.rider.id)
        riders.append({
            'number': rider.number,
            'id': rider.id,
            'name': rider.name
        })
    for track in tracks:
        track.leaders = get_leaders_for_track(stage.id, track)
    return render(request, 'stage_details.html', {'riders': riders, 'stage': stage, 'tracks': tracks})


def track_details(request, pk, stage_id):
    track = None
    stage = Stage.objects.get(id=stage_id)
    riders_in_stage = RiderAndStage.objects.filter(stage=stage)
    if Track.objects.exists():
        track = Track.objects.get(id=pk)
    riders = []
    for rider_in_stage in riders_in_stage:
        rider = Rider.objects.get(id=rider_in_stage.rider.id)
        riders.append({
            'number': rider.number,
            'id': rider.id,
            'name': rider.name,
            'results': Result.objects.filter(
                    stage_id=stage_id,
                    track_id=track,
                    rider_id=rider.id,
                ).values().order_by('created_at'),
            'best_time': Result.objects.exclude(status__in=('DNF', 'DNS',)).filter(
                    stage_id=stage_id,
                    track_id=track,
                    rider_id=rider.id,
                ).values().order_by('result_time').first(),
            'total_score': Result.objects.filter(
                    stage_id=stage_id,
                    track_id=track,
                    rider_id=rider.id,
                ).values('points').aggregate(Sum('points')),
            'statuses': RACE_STATUSES,
        })
    leaders = get_leaders_for_track(stage_id, track)
    return render(request, 'track_details.html', {
        'riders': riders,
        'stage': stage,
        'track': track,
        'leaders': leaders,
    })


def get_leaders_for_track(stage_id, track):
    leaders = []
    losers = Result.objects.filter(
        stage_id=stage_id,
        track_id=track.id,
        status__in=('DSQ', 'DRP')
    ).values('rider_id')
    if track.isCountingTime:
        raw_leaders = Result.objects.exclude(
            rider__in=losers
        ).filter(
            stage_id=stage_id,
            track_id=track.id,
        ).values('rider').annotate(time=Min('result_time')).order_by('time')[:3]
        for leader in raw_leaders:
            rider = Rider.objects.get(id=leader['rider'])
            leaders.append({
                'track': track.id,
                'number': rider.number,
                'id': rider.id,
                'name': rider.name,
                'time': leader['time'],
            })
    else:
        raw_leaders = Result.objects.exclude(
            rider__in=losers
        ).filter(
            stage_id=stage_id,
            track_id=track.id,
        ).values('rider').annotate(points=Sum('points')).order_by('-points')[:3]
        for leader in raw_leaders:
            rider = Rider.objects.get(id=leader['rider'])
            leaders.append({
                'track': track.id,
                'number': rider.number,
                'id': rider.id,
                'name': rider.name,
                'points': leader['points'],
            })
    return leaders


def get_leaders_for_stage(stage):
    Leaderboard.objects.all().delete()
    tracks = Track.objects.filter(stage_id=stage.id)
    for track in tracks:
        track_leaders = get_leaders_for_track(stage.id, track)
        Leaderboard(
            stage_id=stage.id,
            track_id=track_leaders[0]['track'],
            rider_id=track_leaders[0]['id'],
            finished=1,
        ).save()
        Leaderboard(
            stage_id=stage.id,
            track_id=track_leaders[1]['track'],
            rider_id=track_leaders[1]['id'],
            finished=2,
        ).save()
        Leaderboard(
            stage_id=stage.id,
            track_id=track_leaders[2]['track'],
            rider_id=track_leaders[2]['id'],
            finished=3,
        ).save()
    # get stage leaders
    leaders = [{
        '1st': Leaderboard.objects.filter(
             rider_id__in=(Leaderboard.objects.filter(
                 stage_id=stage.id,
                 finished=1,
             ).values('rider_id').distinct())
        ).values('rider_id').annotate(rider=Max(Count('rider_id'))).values('rider'),
        '2nd': Leaderboard.objects.filter(
            rider_id__in=(Leaderboard.objects.filter(
                stage_id=stage.id,
                finished=2,
            ).values('rider_id').distinct())
        ).values('rider_id').annotate(rider=Max(Count('rider_id'))).values('rider'),
        '3rd': Leaderboard.objects.filter(
            rider_id__in=(Leaderboard.objects.filter(
                stage_id=stage.id,
                finished=3,
            ).values('rider_id').distinct())
        ).values('rider_id').annotate(rider=Max(Count('rider_id'))).values('rider'),
    }]
    return leaders


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


def rider_delete(request, rider_id):
    rider = Rider.objects.get(id=rider_id)
    if os.path.isfile(Rider.objects.get(id=rider.id).photo.path):
        os.remove(Rider.objects.get(id=rider.id).photo.path)
    Rider.objects.get(id=rider.id).delete()
    return redirect('em:riders')


def stage_delete(request, stage_id):
    stage = Stage.objects.get(id=stage_id)
    Stage.objects.get(id=stage.id).delete()
    return redirect('em:stages')


def track_delete(request, track_id, stage_id):
    Track.objects.get(id=track_id).delete()
    return redirect('em:stage_details', stage_id)


def track_finalize(request, track_id, stage_id):
    track = Track.objects.get(id=track_id)
    track.isOpened = TRACK_STATUSES[1][0]
    track.save()
    return redirect('em:stage_details', stage_id)


def result_delete(request, result_id, track_id, stage_id):
    Result.objects.get(id=result_id).delete()
    return redirect('em:track_details', track_id, stage_id)


def rider_cancel_ride(request, track_id, stage_id):
    ride_cancel()
    return redirect('em:track_details', track_id, stage_id)


def rider_prepare_to_ride_with_time(request, rider_id, track_id, stage_id):
    set_rider_ready(rider_id, track_id, stage_id, None)
    return redirect('em:track_details', track_id, stage_id)


def rider_prepare_to_ride_with_points(request, rider_id, track_id, stage_id):
    if request.POST.get('points'):
        points = int(request.POST.get('points'))
    else:
        points = 0
    if points > 0:
        set_rider_ready(rider_id, track_id, stage_id, points)
    return redirect('em:track_details', track_id, stage_id)


def rider_set_status(request, rider_id, track_id, stage_id):
    if request.POST.get('status'):
        set_rider_status(rider_id, track_id, stage_id, request.POST.get('status'))
    return redirect('em:track_details', track_id, stage_id)


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


def track_add(request, stage_id):
    stage = Stage.objects.get(id=stage_id)
    if request.method == 'POST':
        form = TrackAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('em:stage_details', stage_id)
    else:
        form = TrackAddForm()
    return render(request, 'track_add_form.html', {
        'form': form,
        'stage': stage
    })
