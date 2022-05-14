from machine import ADC,Pin###光感
import utime
import outer_interrupt as oi

adc=ADC(Pin(34))#创建一个ADC的对象，然后直接把pin对象传入到ADC的构造器里面。pin脚可以是32, 33, 34, 35, 36, 39
adc.atten(ADC.ATTN_6DB)#设置衰减比，满量程2V
adc.width(ADC.WIDTH_11BIT) # 设置数据宽度为11bit

def adc_mean(adc, sample_times):#均值滤波
    l=int(sum([adc.read() for i in range(sample_times)])/sample_times)

def culculate_light():
    diff=1023-adc_mean.l
    if (800<diff)|(diff<1023)|(diff==1023) :#很亮
        oi.led_period=10#不开灯     
    elif(diff>640)|(diff<800)| (diff==800) :#亮
        oi.led_period=8#一档亮度；一个正波形10ms，导通最后的2ms
    elif(diff>512)|(diff<640)| (diff==640) :#比较亮
        oi.led_period=5#二档默认亮度；一个正波形10ms，导通最后的5ms
    elif(diff>300)|(diff<512)| (diff==512) :#比较暗
        oi.led_period=8#三档亮度；一个正波形10ms，导通最后的8ms
    else:#黑暗
        oi.led_period=0#全功率亮度；一个正波形10ms全导通


'''
while 1 :
    adc_mean(adc,10)
    utime.sleep(3)
'''