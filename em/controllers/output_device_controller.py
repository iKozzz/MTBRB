from gpiozero import Buzzer, LED

bz = Buzzer(11)
ld = LED(15)


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
    bz.on()
    ld.on()


def connection_test_end():
    bz.off()
    ld.off()
