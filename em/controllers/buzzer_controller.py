from gpiozero import Buzzer

bz = Buzzer(10)


def server_startup_alert():
    bz.blink(1, 0.5, 3)


def ride_start_alert():
    bz.blink(2, 1, 1)


def ride_finish_alert():
    bz.blink(4, 1, 2)


def ride_cancel_alert():
    bz.blink(1, 1, 2)
