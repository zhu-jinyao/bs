import _thread
from machine import utime
import wifi
import mqtt_sub,mqtt_pub
import infrared_test
import moto
import temperature
import light

def testThread_sub():##订阅风扇、LED灯控制信息
    while 1:
        mqtt_sub.client.check_msg()
        utime.sleep(3)

def testThread_pub():##发布温度、亮度信息
    while 1:
        mqtt_pub.client.publish(mqtt_pub.TOPIC_fan, mqtt_pub.t)#每3S发布一次温度数据
        mqtt_pub.client.publish(mqtt_pub.TOPIC_LED, mqtt_pub.l)#每3S发布一次温度数据
        utime.sleep(3)

def testThread_infrared():##读取热释电传感器，获取人体存在信息;有人则进行过零检测，在合适时机开始控制风扇、LED灯导通
    while 1:
        if infrared.value()==1:
            wdt.feed()
            outer_inter.irq(handler=oi.zero_crossing,trigger=Pin.IRQ_FALLING)
        utime.sleep(2)


def testThread_moto():##驱动电机正反转动
    while 1:
        moto.moto_reverse_driver()

def testThread_temperature():
    while 1:
        readData()
        utime.sleep(3)
        culculate_temp()

def testThread_light():
    while 1:
        adc_mean(light.adc,10)
        utime.sleep(3)
        culculate_light()

def testThread_ctrl():
    while 1:
        zero_crossing()


wifi.do_connect()#先连接WiFi
_thread.start_new_thread(testThread_infrared)#启动读取热释电传感器线程，以默认功率开启风扇和LED灯
_thread.start_new_thread(testThread_moto)#启动驱动电机正反转动线程
_thread.start_new_thread(testThread_temperature)#启动获取温度的线程，传递风扇需要工作的时长
_thread.start_new_thread(testThread_light)#启动获取亮度的线程，传递LED需要工作的时长
_thread.start_new_thread(testThread_pub)#启动发布光温信息线程
_thread.start_new_thread(testThread_sub)#启动订阅风扇、灯的控制信息线程


