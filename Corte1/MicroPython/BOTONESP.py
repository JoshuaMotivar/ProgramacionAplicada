from machine import Pin
import time

Boton = 4
leds = [Pin(i,Pin.OUT)for i in (32, 33, 25, 26, 27, 14, 12, 13)]
presss_button = Pin(Boton, Pin.IN, Pin.PULL_UP) 

while True :
    if  Boton == 0 and last_State == 1:
        led_state = not(led_state)
        led.value(led_state)
        
        
    for led in leds:
        led. value(1)
        time.sleep(0.2)
        led.value(0)
    
    for led in reversed (leds):
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        
    for led in leds:
        led.value(1)
        time.sleep(0.2)
            
    for led in leds :
        led.value(0)
        time.sleep(0.2)