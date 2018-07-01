# from gpiozero import Button
from datetime import datetime, timedelta
from random import uniform

from em.models import *
START_BUTTON_PIN_NUMBER = 14
FINISH_BUTTON_PIN_NUMBER = 15

# START_BUTTON = Button(START_BUTTON_PIN_NUMBER)
# FINISH_BUTTON = Button(FINISH_BUTTON_PIN_NUMBER)

START_TIME = None
RIDER_ID = None
RACE_ID = None
STAGE_ID = None
POINTS = 0


def get_current_timestamp(delta):
    # return datetime.now()
    return datetime.now() + timedelta(seconds=delta)


def set_rider_ready(rider_id, race_id, stage_id, points):
    global RIDER_ID
    global RACE_ID
    global STAGE_ID
    global POINTS
    RIDER_ID = rider_id
    RACE_ID = race_id
    STAGE_ID = stage_id
    if points is not None:
        POINTS = points
    # for debug
    race_start()
    race_finish()


def race_cancel():
    global START_TIME
    global RIDER_ID
    global STAGE_ID
    START_TIME = None
    RIDER_ID = None
    STAGE_ID = None


def race_start():
    global START_TIME
    if RIDER_ID is not None and START_TIME is None:
        START_TIME = get_current_timestamp(0)


def race_finish():
    global START_TIME
    global RIDER_ID
    global STAGE_ID
    global POINTS
    if RIDER_ID is not None and START_TIME is not None:
        finish_time = get_current_timestamp(uniform(1, 5))
        result = finish_time - START_TIME
        Result(
            race=Race.objects.get(id=RACE_ID),
            rider=Rider.objects.get(id=RIDER_ID),
            stage=Stage.objects.get(id=STAGE_ID),
            status=RACE_STATUSES[0][1],
            points=POINTS,
            start_time=START_TIME,
            finish_time=finish_time,
            result_time=result,
            ).save()
        START_TIME = None
        RIDER_ID = None
        STAGE_ID = None
        POINTS = 0


# START_BUTTON.when_activated = race_start
# FINISH_BUTTON.when_activated = race_finish