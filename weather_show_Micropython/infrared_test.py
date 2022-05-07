from machine import Pin    
import utime
from machine import WDT
import outer_interrupt as oi

wdt = WDT(timeout=60000)  # enable it with a timeout of 60s

outer_interrupt=Pin(12,Pin.IN)#3
infrared=Pin(35,Pin.IN)

while 1:
    if infrared.value()==1:
        wdt.feed()
        outer_interrupt.irq(handler=oi.zero_crossing,trigger=Pin.IRQ_FALLING)
    utime.sleep(2)