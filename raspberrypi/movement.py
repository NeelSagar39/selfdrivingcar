import RPi.GPIO as gpio
import time


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(36, gpio.OUT)
    gpio.setup(37, gpio.OUT)

    global s, e, t, f
    s = gpio.PWM(12, 50)
    e = gpio.PWM(18, 50)
    t = gpio.PWM(36, 50)
    f = gpio.PWM(37, 50)

    s.start(0)
    e.start(0)
    t.start(0)
    f.start(0)


def end():
    s.stop()
    e.stop()
    t.stop()
    f.stop()
    gpio.cleanup()


def forward(tf):
    init()
    s.ChangeDutyCycle(100)
    e.ChangeDutyCycle(0)
    t.ChangeDutyCycle(0)
    f.ChangeDutyCycle(100)
    time.sleep(tf)
    end()
    gpio.cleanup()


def reverse(tf):
    init()
    s.ChangeDutyCycle(0)
    e.ChangeDutyCycle(100)
    t.ChangeDutyCycle(100)
    f.ChangeDutyCycle(0)
    time.sleep(tf)
    end()
    gpio.cleanup()


def right(tf):
    init()
    s.ChangeDutyCycle(50)  # true
    e.ChangeDutyCycle(0)  # true
    t.ChangeDutyCycle(0)  # true
    f.ChangeDutyCycle(20)  # false
    time.sleep(tf)
    end()
    gpio.cleanup()


def left(tf):
    init()
    s.ChangeDutyCycle(20)  # false
    e.ChangeDutyCycle(0)  # true
    t.ChangeDutyCycle(0)  # false
    f.ChangeDutyCycle(50)  # false
    time.sleep(tf)
    end()
    gpio.cleanup()
    