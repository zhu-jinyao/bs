
from machine import PWM,Pin,utime

def moto_reverse_driver():
    moto_pin1=Pin(25,Pin.OUT)
    moto_pwm1=PWM(moto_pin1)
    moto_pwm1.freq(700)
    moto_pwm1.duty(200)
    utime.sleep_us(280)#保证PWM1与PWM2相位相错，否则都是电机不转，都是高电平则会浪费资源
    moto_pin2=Pin(14,Pin.OUT)
    moto_pwm2=PWM(moto_pin2)
    moto_pwm2.freq(700)
    moto_pwm2.duty(200)


'''
import machine
import utime, math
import switch as sw
from machine import Pin

switch_led = sw.Switch(Pin(2))

def pulse(switch, period, gears):
    # 呼吸灯核心代码
    # 借用sin正弦函数，将PWM范围控制在 23 - 1023范围内
    # switch 开关对象
    # period 呼吸一次的周期 单位/毫秒
    # gears 呼吸过程中经历的亮度档位数

    for i in range(2 * gears):
        switch.change_duty(int(math.sin(i / gears * math.pi) * 500) + 523)
        # 延时
        utime.sleep_ms(int(period / (2 * gears)))

# 呼吸十次
while 1:
    pulse(switch_led, 2000, 100)

# 释放资源
switch_led.deinit()
'''