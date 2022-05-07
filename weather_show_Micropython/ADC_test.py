from machine import ADC,Pin###光感
import utime

adc=ADC(Pin(34))#创建一个ADC的对象，然后直接把pin对象传入到ADC的构造器里面。pin脚可以是32, 33, 34, 35, 36, 39
adc.atten(ADC.ATTN_6DB)#设置衰减比，满量程2V
adc.width(ADC.WIDTH_11BIT) # 设置数据宽度为11bit

def adc_mean(adc, sample_times):#均值滤波
    return int(sum([adc.read() for i in range(sample_times)])/sample_times)

while 1 :
    adc_mean(adc,10)
    utime.sleep(3)