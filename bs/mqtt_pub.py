from umqtt.simple import MQTTClient
import utime
from temperature import readData
from light import adc_mean

SERVER = '192.168.43.16'
CLIENT_ID = '10fcafbd10da4bc2b25feb1e9ea499a8' # 客户端的ID，不可重复，尽量使用云平台的设备号
TOPIC_LED = b'LED_info' # TOPIC的ID
TOPIC_fan = b'fan_info'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()

t=readData.t#每3S有一次数据
l=adc_mean#每3S有一次数据

while True:
    client.publish(TOPIC_fan, t)#每3S发布一次温度数据
    client.publish(TOPIC_LED, l)#每3S发布一次亮度数据
    utime.sleep(3)