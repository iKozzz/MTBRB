from gpiozero import Buzzer

bz = Buzzer(10)


def server_startup_alert():
    bz.blink(on_time=0.5, off_time=0.5, n=3, background=True)


def ride_start_alert():
    bz.blink(on_time=3, off_time=0.5, n=1, background=True)


def ride_finish_alert():
    bz.blink(on_time=2, off_time=0.5, n=2, background=True)


def ride_cancel_alert():
    bz.blink(on_time=3, off_time=0, n=1, background=True)
