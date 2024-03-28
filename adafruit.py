import sys

import paho.mqtt.client as mqtt
import random
import time

MQTT_SERVER = "io.adafruit.com"
MQTT_PORT = 1883
MQTT_USERNAME = "YOUR_NAME"
MQTT_PASSWORD = ""
MQTT_TOPICS = ["fan", "light"]
MQTT_TEMP_TOPIC = "temp"
MQTT_HUMID_TOPIC = "humid"
MQTT_LIGHT_TOPIC = "led"
MQTT_FAN_TOPIC = "fan"


class Paho_MQTT:

    def __init__(self, broker_user, broker_pass):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.username_pw_set(broker_user, broker_pass)
        # self.self.client.connect(MQTT_SERVER, int(MQTT_PORT), 60)

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe

    def connect(self):
        self.client.connect(MQTT_SERVER, int(MQTT_PORT), 60)

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def publish(self, topic, message):
        self.client.publish(topic, message)

    def on_connect(self, client, userdata, flags, rc, properties):
        if rc.is_failure:
            print(f"Failed to connect: {rc}. loop_forever() will retry connection")
        else:
            print("Connected successfully")

    def on_subscribe(self, client, userdata, mid, rc_list, properties):
        if rc_list[0].is_failure:
            print(f"Broker rejected your subscription: {rc_list[0]}")
        else:
            print(f"Broker granted the following QoS: {rc_list[0].value}")

    def on_disconnect(self, client):
        print("Disconnected...")
        sys.exit(1)

    def on_message(self, client, userdata, message):
        print(
            "Received message '"
            + str(message.payload.decode("utf-8"))
            + "' on topic '"
            + message.topic
            + "' with QoS "
            + str(message.qos)
        )

    def loop_start(self):
        self.client.loop_start()

    # def published(self, topic, message):
    #     self.client.publish(topic, message)
