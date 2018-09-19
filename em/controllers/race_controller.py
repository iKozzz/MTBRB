from datetime import datetime

from gpiozero import Button

from em.controllers.output_device_controller import *
from em.models import *

START_BUTTON = Button(2)
FINISH_BUTTON = Button(3)

START_TIME = None
RIDER_ID = None
TRACK_ID = None
STAGE_ID = None
POINTS = 0


def get_current_rider_id():
    return RIDER_ID


def get_current_track_id():
    return TRACK_ID


def get_current_timestamp():
    return datetime.now()


def set_rider_ready(rider_id, track_id, stage_id, points):
    global RIDER_ID
    global TRACK_ID
    global STAGE_ID
    global POINTS
    RIDER_ID = rider_id
    TRACK_ID = track_id
    STAGE_ID = stage_id
    if points is not None:
        ride_start()
        POINTS = points
        ride_finish()


def ride_cancel():
    global START_TIME
    global RIDER_ID
    global STAGE_ID
    START_TIME = None
    RIDER_ID = None
    STAGE_ID = None
    ride_cancel_alert()


def ride_start():
    make_some_action()
    global START_TIME
    # check start time to prevent issues with start button
    if RIDER_ID is not None and START_TIME is None:
        START_TIME = get_current_timestamp()
        ride_start_alert()


def ride_finish():
    make_some_action()
    global START_TIME
    global RIDER_ID
    global TRACK_ID
    global STAGE_ID
    global POINTS
    if RIDER_ID is not None:
        finish_time = get_current_timestamp()
        result = finish_time - START_TIME
        Result(
            track=Track.objects.get(id=TRACK_ID),
            rider=Rider.objects.get(id=RIDER_ID),
            stage=Stage.objects.get(id=STAGE_ID),
            status='OK',
            points=POINTS,
            start_time=START_TIME,
            finish_time=finish_time,
            result_time=result,
            ).save()
        START_TIME = None
        RIDER_ID = None
        TRACK_ID = None
        STAGE_ID = None
        POINTS = 0
        ride_finish_alert()


def set_rider_status(rider_id, track_id, stage_id, status):
    ride_cancel()
    Result(
        rider=Rider.objects.get(id=rider_id),
        track=Track.objects.get(id=track_id),
        stage=Stage.objects.get(id=stage_id),
        status=status,
    ).save()


START_BUTTON.when_activated = ride_start
FINISH_BUTTON.when_activated = ride_finish
