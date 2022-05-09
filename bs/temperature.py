import utime
from machine import Pin
import dht#支持引脚 ESP32:GPIO0/2/4/5/16/17/18/19/21/22/23/25/26/27
from dht import DHT11   ###http://www.wtbing.cn/thread-35.htm 不用另外写dht11.py文件再导入，本身就有dht这个模块，yeah!!
import outer_interrupt as oi

d = DHT11(Pin(23))
def readData():
    d.measure()
    t=d.temperature()

def culculate_temp():
    diff=readData.t-24
    if diff<0:
        oi.fan_period=10#不开
    elif(diff>0)|(diff<2)|(diff==2) :#24~26摄氏度
        oi.fan_period=8#一档转速；一个正波形10ms，导通最后的2ms
    elif(diff>2)|(diff<6)|(diff==6) :#26~30摄氏度
        oi.fan_period=5#二档默认转速；一个正波形10ms，导通最后的5ms
    elif(diff>6)|(diff<6)|(diff==6) :#30~35摄氏度
        oi.fan_period=8#三档转速；一个正波形10ms，导通最后的8ms
    else #高于35摄氏度
        oi.fan_period=0#全功率转速；一个正波形10ms全导通

''' h=d.humidity()
    print("temp:")
    print( t )


while True:
    readData()
    utime.sleep(3)
    culculate_temp()
'''

