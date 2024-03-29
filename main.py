from adafruit import *
from simple_ai import *

# import paho.mqtt.client as mqtt
# obj = Adafruit_MQTT()


def mqtt_connected(client, userdata, flags, rc, properties):
    if rc.is_failure:
        print(f"Failed to connect: {rc}. loop_forever() will retry connection")
    else:
        # we should always subscribe from on_connect callback to be sure
        # our subscribed is persisted across reconnections.
        print("Connected successfully")
        client.subscribe(MQTT_USERNAME + "/feeds/" + MQTT_FAN_TOPIC)
        client.subscribe(MQTT_USERNAME + "/feeds/" + MQTT_LIGHT_TOPIC)


def mqtt_subscribed(client, userdata, mid, rc_list, properties):
    if rc_list[0].is_failure:
        print(f"Broker rejected you subscription: {rc_list[0]}")
    else:
        print(f"Broker granted the following QoS: {rc_list[0].value}")


def mqtt_message(client, userdata, msg):
    print(
        "Received message '"
        + str(msg.payload.decode("utf-8"))
        + "' on topic '"
        + msg.topic
        + "' with QoS "
        + str(msg.qos)
    )


# client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
# client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
# client.connect(MQTT_SERVER, int(MQTT_PORT), 60)

# client.on_connect = mqtt_connected
# client.on_subscribe = mqtt_subscribed
# client.on_message = mqtt_message

# client.loop_start()

counter = 1

if __name__ == "__main__":
    mqttClient = Paho_MQTT(MQTT_USERNAME, MQTT_PASSWORD)
    mqttClient.connect()
    mqttClient.subscribe(MQTT_USERNAME + "/feeds/" + MQTT_FAN_TOPIC)
    mqttClient.subscribe(MQTT_USERNAME + "/feeds/" + MQTT_LIGHT_TOPIC)
    mqttClient.loop_start()
    while True:
        face = face_detector()
        counter = counter - 1
        if counter == 0:
            temperature = round(random.uniform(23.0, 34.0), 2)
            mqttClient.publish(MQTT_USERNAME + "/feeds/" + MQTT_TEMP_TOPIC, temperature)
            print(f"Publish temperature: {temperature} degrees Celsius successfully!")

            humid = round(random.uniform(0.0, 101.0), 2)
            mqttClient.publish(MQTT_USERNAME + "/feeds/" + MQTT_HUMID_TOPIC, humid)
            print(f"Publish temperature: {humid}% successfully!")

            mqttClient.publish(MQTT_USERNAME + "/feeds/" + MQTT_FACEID_TOPIC, face)
            print(f"Publish faceid: {face} successfully!")

            counter = 10
        time.sleep(1)
