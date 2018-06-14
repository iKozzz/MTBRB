# from gpiozero import Button
import time
from random import uniform

START_BUTTON_PIN_NUMBER = 14
FINISH_BUTTON_PIN_NUMBER = 15

# START_BUTTON = Button(START_BUTTON_PIN_NUMBER)
# FINISH_BUTTON = Button(FINISH_BUTTON_PIN_NUMBER)

START_TIME = 0
RIDER_ID = 0
RACE_ID = 0


def get_current_timestamp():
    return int(round(time.time() * 1000))


def set_rider_ready(rider_id):
    global RIDER_ID
    global RACE_ID
    RIDER_ID = rider_id
    # RACE_ID = race_id
    # for debug
    race_start()
    time.sleep(uniform(1, 2))
    race_finish()


def race_cancel():
    global START_TIME
    global RIDER_ID
    START_TIME = 0
    RIDER_ID = 0


def race_start():
    global START_TIME
    if RIDER_ID > 0 and START_TIME == 0:
        START_TIME = get_current_timestamp()


def race_finish():
    global START_TIME
    global RIDER_ID
    if RIDER_ID > 0 and START_TIME > 0:
        finish_time = get_current_timestamp()
        result = finish_time - START_TIME
        # write result to mobel
        print(result)
        START_TIME = 0
        RIDER_ID = 0


# START_BUTTON.when_activated = race_start
# FINISH_BUTTON.when_activated = race_finish
