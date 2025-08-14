## --------  MQTT Publish  ------ ##
#   tested with tinkertanks moon   #

import time, ssl, socketpool, wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT

secrets = {
    'client_id' : 'GameController',			# device name
    'ssid' : 'mqttrouter',				# SSID
    'password' : 'Mqtt123456',	# WIFI Password
    'mqtt-username' : 'mqtt-user',			# MQTT Username
    'mqtt-key' : '57616091mqtt',  	# MQTT Password (not always necessary)
    'mqtt-broker' : '192.168.188.26',			# MQTT Broker
    'port' : 1883
    }

wifi.radio.connect(secrets["ssid"], secrets["password"])
pool = socketpool.SocketPool(wifi.radio)
mqtt_client = MQTT.MQTT(broker=secrets["mqtt-broker"],
                        port=secrets["port"],
                        username=secrets["mqtt-username"],
                        password=secrets["mqtt-key"],
                        socket_pool=pool,client_id=secrets["client_id"],
                        socket_timeout=5,
                        ssl_context=ssl.create_default_context(),
)

#### CONNECT #################################
print("connecting...")
mqtt_client.connect()
print("connected")

#### LOOP & PUBLISH ##########################

while True:
    topic = "werkstatt/flipdot/snake"
    payload = int(time.monotonic())
    
    mqtt_client.publish(topic, payload)
    mqtt_client.loop()
    
    print("published:", topic, "payload:", payload)
    time.sleep(1)

