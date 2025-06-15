## ------  MQTT Subscribe  ------ ##
#   tested with tinkertanks moon   #

import time, ssl, socketpool, wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT

secrets = {
    'client_id' : 'Frisbee_Number_X',			# device name
    'ssid' : 'TinkertankMobile2',				# SSID
    'password' : '57616091',					# WIFI Password
    'mqtt-username' : 'tinkertank',				# MQTT Username
    'mqtt-key' : '57616091',  					# MQTT Password
    'mqtt-broker' : '192.168.43.150',			# MQTT Broker
    'port' : 1883
    }

wifi.radio.connect(secrets["ssid"], secrets["password"])
pool = socketpool.SocketPool(wifi.radio)
mqtt_client = MQTT.MQTT(broker=secrets["mqtt-broker"],port=secrets["port"],username=secrets["mqtt-username"],password=secrets["mqtt-key"],socket_pool=pool,client_id=secrets["client_id"],ssl_context=ssl.create_default_context(),
)
print("IP Address:", wifi.radio.ipv4_address)

#### RECEIVE #################################

def message(client, topic, message):
    print("New message on topic {0}: {1}".format(topic, message))
    
#### CONNECT #################################
print("connecting...")
mqtt_client.on_message = message    
mqtt_client.connect()
print("connected")

#### SUBSCRIPTIONS ###########################

mqtt_client.subscribe("foo/bar",2)

#### LOOP #ä##################################

while True:
    time.sleep(0.001)
    mqtt_client.loop()


