from gpiozero import Buzzer, LED, Button

bz = Buzzer(11)
ld = LED(15)
sb = Button(2)
fb = Button(3)


def server_startup_alert():
    bz.blink(0.12, 0.05, 5)
    ld.blink(0.12, 0.05, 5)


def ride_start_alert():
    bz.blink(1, 0, 1)
    ld.blink(1, 0, 1)


def ride_finish_alert():
    bz.blink(0.5, 0.3, 3)
    ld.blink(0.5, 0.3, 3)


def ride_cancel_alert():
    bz.blink(0.08, 0.05, 2)
    ld.blink(0.08, 0.05, 2)


def connection_test_start():
    sb.when_activated(make_some_noise())
    fb.when_activated(make_some_noise())


def connection_test_end():
    sb.when_activated(None)
    fb.when_activated(None)


def make_some_noise():
    bz.blink(0.15, 0.05, 3)
    ld.blink(0.15, 0.05, 3)
