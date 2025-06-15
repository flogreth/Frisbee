## ---  MQTT Publish & Subscribe  --- ##
#     tested with tinkertanks moon     #

import time, ssl, socketpool, wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT

secrets = {
    'client_id' : 'Moon Publisher',			# device name
    'ssid' : 'YourWifiSSID',				# SSID
    'password' : 'YourSecretWifiPassword',	# WIFI Password
    'mqtt-username' : 'mqtt-user',			# MQTT Username
    'mqtt-key' : 'mqtt-user-password',  	# MQTT Password
    'mqtt-broker' : 'servername',			# MQTT Broker
    'port' : 1883
    }

wifi.radio.connect(secrets["ssid"], secrets["password"])
pool = socketpool.SocketPool(wifi.radio)
mqtt_client = MQTT.MQTT(broker=secrets["mqtt-broker"],port=secrets["port"],username=secrets["mqtt-username"],password=secrets["mqtt-key"],socket_pool=pool,client_id=secrets["client_id"],ssl_context=ssl.create_default_context(),
)
#### RECEIVE #################################

def message(client, topic, message):
    print("New message on topic {0}: {1}".format(topic, message))

#### CONNECT #################################

print("connecting...")
mqtt_client.on_message = message    
mqtt_client.connect()
print("connected")

#### SUBSCRIPTIONS ###########################

mqtt_client.subscribe("topic/subtopic/subsubtopic",2)

#### LOOP & PUBLISH ##########################

while True:
    mqtt_client.publish("topic/subtopic/subsubtopic", "payload")
    mqtt_client.loop()
    time.sleep(1)

        
