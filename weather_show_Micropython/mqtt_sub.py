from umqtt.simple import MQTTClient
import utime

SERVER = '192.168.1.101'
CLIENT_ID = '10fcafbd10da4bc2b25feb1e9ea499a8'
TOPIC_LED = b'LED_control'
TOPIC_fan = b'fan_control'

def mqtt_callback(topic, msg):
    


client = MQTTClient(CLIENT_ID, SERVER)#创建一个MQTT连接
client.set_callback(mqtt_callback)
client.connect()

client.subscribe(TOPIC_LED)
client.subscribe(TOPIC_fan)


while True:
    # 查看是否有数据传入
    # 有的话就执行 mqtt_callback
    client.check_msg()
    utime.sleep(3)