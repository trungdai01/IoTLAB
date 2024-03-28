import sys
from Adafruit_IO import MQTTClient

MQTT_SERVER = "mqttserver.tk"
MQTT_PORT = 1883
MQTT_USERNAME = "innovation"
MQTT_PASSWORD = "Innovation_RgPQAZoA5N"
MQTT_TOPICS = ["button1", "button2"]
MQTT_TEMP_TOPIC = "temp"
MQTT_HUMID_TOPIC = "humid"
MQTT_LIGHT_TOPIC = "light"
MQTT_FAN_TOPIC = "fan"

class Adafruit_MQTT:

    def connected(self, client):
        print("Connected ...")
        for feed in MQTT_TOPICS:
            client.subscribe(feed)

    def subscribe(self, client , userdata , mid , granted_qos):
        print("Subscribed...")

    def disconnected(self, client):
        print("Disconnected...")
        sys.exit (1)

    def message(self, client , feed_id , payload):
        print("Received: " + payload)

    def __init__(self):
        client = MQTTClient(MQTT_USERNAME , MQTT_PASSWORD)
        client.on_connect = self.connected
        client.on_disconnect = self.disconnected
        client.on_message = self.message
        client.on_subscribe = self.subscribe
        client.connect()
        client.loop_background()

