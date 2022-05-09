from machine import Pin,Timer

led_period=5
fan_period=5
#outer_interrupt=Pin(3,Pin.IN)
led_p=Pin(2,Pin.OUT)#5
fan_p=Pin(19,Pin.OUT)

def toggle_led(pin):
    pin.value(1)
def led_ctrl(pin,period=5):#默认亮度：半亮。一个正波形是10ms，半个正波形是5ms
    led_timer=Timer(1)
    led_timer.init(period=period, mode=Timer.PERIODIC, callback=lambda t:toggle_led(pin))

def toggle_fan(pin):
    pin.value(1)
def fan_ctrl(pin,period=5):#默认转速
    led_timer=Timer(2)
    led_timer.init(period=period, mode=Timer.PERIODIC, callback=lambda t:toggle_led(pin))

def zero_crossing(led_period,fan_period):
    led_ctrl(led_p,led_period)#调用定时器延时一段时间，再输出控制可控硅电路的信号
    fan_ctrl(fan_p,fan_period)

#outer_interrupt.irq(handler=zero_crossing,trigger=Pin.IRQ_FALLING)


'''
from machine import Pin,Timer

motion=False

def interrupt_handle(pin):
    global motion
    motion=True
    global interrupt_pin
    interrupt_pin=pin

led=Pin(2,Pin.OUT)
pir=Pin(14,Pin.IN)
vcc=Pin(0,Pin.OUT)#给PIR模块供电vcc

vcc.value(1)

pir.irq(handler=interrupt_handle, trigger=Pin.IRQ_FALLING)

def turn_off(pin):
    pin.value(0)

count=0
led_timer=0

while 1:
    if motion:
        if led_timer:
            led_timer.deinit()
            print("led_timer deinit success!")
        led.value(1)
        count=count+1
        print("motion detected! the trigger pin is:",interrupt_pin,count)
        led_timer=Timer(1)
        led_timer.init(period=2000,mode=Timer.PERIODIC, callback=lambda t:turn_off(led))
        print('Motion stopped!')
        motion=False
'''