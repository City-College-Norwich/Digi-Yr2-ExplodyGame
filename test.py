import RPi.GPIO as gpio

button_pin = 37
buzzer_pin = 12

gpio.setmode(gpio.BOARD)

gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buzzer_pin, gpio.OUT)

try:
    while True:
        if (gpio.input(button_pin)):
            gpio.output(buzzer_pin, gpio.HIGH)
        else:
            gpio.output(buzzer_pin, gpio.LOW)
except KeyboardInterrupt:
    gpio.cleanup()