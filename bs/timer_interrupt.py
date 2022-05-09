from machine import Timer,Pin   ###用定时器实现PWM波输出
import utime


def toggle1_led(led_pin):
    '''
    LED状态反转
    '''
    led_pin.value(1)

def toggle2_led(led_pin):
    '''
    LED状态反转
    '''
    led_pin.value(0)


def led_blink_timed(led_pin):##系统使用时，要有portion参数传入
    '''
    led 按照特定的频率进行闪烁
    LED闪烁周期 = 1000ms / 频率
    状态变换间隔（period） = LED闪烁周期/ 2 
    '''

    timer1 = Timer(1)    # 代表一个正波形或负波形的时间。创建定时器对象,输入任意正整数
    timer2 = Timer(2)    # 代表高电平部分的时间。创建定时器对象,输入任意正整数
    duty1=1#一个正波形或负波形的周期。空缺是80%，占空比是20%
    duty2=0.2#一个正波形或负波形的占空比是20%
    # 计算状态变换间隔 时间 ms
    period1 = int(duty1*5)#市电50Hz下，半个正波形或负波形的周期是5ms 。
             #因为按照一个负波形的周期来算，测试的LED会在高占空比的时候看见频闪，这对控制220V的LED不利。故提高频率，总的占空比不变，但能改善频闪。
             #市电50Hz下，一个正波形或负波形的周期是10ms                
             #int(duty1 * 1000 / freq)   ###1秒/1秒的正负波数
    period2 = int(duty2*5)#int(duty2 * 1000 / freq)   ###1秒/1秒的正负波数


    portion_a=2 ###挡数。多少份高电平。
    #系统使用时，作为led_blink_timed的参数传入即可


    # 初始化定时器
    # 这里回调是使用了lambda表达式，因为回调函数需要传入led_pin
    timer1.init(period=period1, mode=Timer.PERIODIC, callback=lambda t:toggle1_led(led_pin))
   # utime.sleep(duty1)
    timer2.init(period=period2*portion_a, mode=Timer.PERIODIC, callback=lambda t:toggle2_led(led_pin))


# 声明引脚 D2 作为LED的引脚
led_pin = Pin(2, Pin.OUT)

led_blink_timed(led_pin)##系统使用时，要有portion参数传入



'''''''''''''''''''''测试：以上是控制板载LED的PWM，以下是控制电机的PWM(电压很小，电机可能是有惯性，有震动、不转动)'''''''''''''''

def toggle3_led(led_pin):
    '''
    LED状态反转
    '''
    led_pin.value(1)

def toggle4_led(led_pin):
    '''
    LED状态反转
    '''
    led_pin.value(0)


def led_blink_timed(led_pin):##系统使用时，要有portion参数传入
    '''
    led 按照特定的频率进行闪烁
    LED闪烁周期 = 1000ms / 频率
    状态变换间隔（period） = LED闪烁周期/ 2 
    '''

    timer3 = Timer(3)    # 代表一个正波形或负波形的时间。创建定时器对象,输入任意正整数
    timer4 = Timer(4)    # 代表高电平部分的时间。创建定时器对象,输入任意正整数
    duty3=1#一个正波形或负波形的周期。空缺是80%，占空比是20%
    duty4=0.2#一个正波形或负波形的占空比是20%
    # 计算状态变换间隔 时间 ms
    period3 = int(duty3*10)#市电50Hz下，半个正波形或负波形的周期是5ms 。
             #因为按照一个负波形的周期来算，测试的LED会在高占空比的时候看见频闪，这对控制220V的LED不利。故提高频率，总的占空比不变，但能改善频闪。
             #市电50Hz下，一个正波形或负波形的周期是10ms                
             #int(duty1 * 1000 / freq)   ###1秒/1秒的正负波数
    period4 = int(duty4*10)#int(duty2 * 1000 / freq)   ###1秒/1秒的正负波数


    portion_b=1 ###挡数。多少份高电平。
    #系统使用时，作为led_blink_timed的参数传入即可


    # 初始化定时器
    # 这里回调是使用了lambda表达式，因为回调函数需要传入led_pin
    timer3.init(period=period3, mode=Timer.PERIODIC, callback=lambda t:toggle3_led(led_pin))
   # utime.sleep(duty1)
    timer4.init(period=period4*portion_b, mode=Timer.PERIODIC, callback=lambda t:toggle4_led(led_pin))


# 声明引脚 D2 作为LED的引脚
led_pin = Pin(16, Pin.OUT)

led_blink_timed(led_pin)##系统使用时，要有portion参数传入





'''
刚上电是全功率高电平输出。
同时定义两个定时器。
timer2的时间到了之后就开始输出低电平
timer1时间到了之后输出一次高电平，
然后很快timer2的时间到了，又开始输出低电平。

所以由timer1设置为高电平，但高电平的时长由timer2决定。

timer2初始化的period是控制高电平的时间，只需修改portion份数即可改变占空比


人在时要一直控制LED和fan，人离开后要timer.deinit()
'''

