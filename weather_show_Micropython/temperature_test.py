import utime
from machine import Pin
import dht#支持引脚 ESP32:GPIO0/2/4/5/16/17/18/19/21/22/23/25/26/27
from dht import DHT11   ###http://www.wtbing.cn/thread-35.htm 不用另外写dht11.py文件再导入，本身就有dht这个模块，yeah!!

d = DHT11(Pin(23))
def readTaHData():
    d.measure()
    t=d.temperature()
    h=d.humidity()
    print("temp:")
    print( t )
    
    print( "humidity:" )
    print( h )
    print()

while True:
    readTaHData()
    utime.sleep(2)


