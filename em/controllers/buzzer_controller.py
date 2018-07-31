from gpiozero import Buzzer

bz = Buzzer(10)


def server_startup_alert():
    bz.blink(on_time=1, off_time=0.5, n=3, background=True)


def ride_start_alert():
    bz.on()
    # bz.blink(on_time=1, off_time=0.5, n=3, background=True)


def ride_finish_alert():
    bz.off()
    # bz.blink(on_time=1, off_time=0.5, n=3, background=True)


def ride_cancel_alert():
    bz.blink(on_time=3, off_time=0, n=1, background=True)
