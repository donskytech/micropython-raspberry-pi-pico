import time
import ubinascii
from umqtt.simple import MQTTClient
import machine
import random
from bme_module import BME280Module
import ujson


# Default  MQTT_BROKER to connect to
MQTT_BROKER = "192.168.100.22"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
SUBSCRIBE_TOPIC = b"led"
PUBLISH_TOPIC = b"sensorReadings"

# Publish MQTT messages after every set timeout
last_publish = time.time()
publish_interval = 5

# Pin assignment
I2C_ID = 0
SCL_PIN = 1
SDA_PIN = 0
bme_module = BME280Module(I2C_ID,SCL_PIN,SDA_PIN)

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))
    if msg.decode() == "ON":
        led.value(1)
    else:
        led.value(0)

# Reset the device in case of error
def reset():
    print("Resetting...")
    time.sleep(5)
    machine.reset()
    
# Read the BMP/BME280 readings
def get_temperature_reading():
    return bme_module.get_sensor_readings()
    
def main():
    print(f"Begin connection with MQTT Broker :: {MQTT_BROKER}")
    mqttClient = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
    mqttClient.set_callback(sub_cb)
    mqttClient.connect()
    mqttClient.subscribe(SUBSCRIBE_TOPIC)
    print(f"Connected to MQTT  Broker :: {MQTT_BROKER}, and waiting for callback function to be called!")
    while True:
            # Non-blocking wait for message
            mqttClient.check_msg()
            global last_publish
            current_time = time.time()
            if (current_time - last_publish) >= publish_interval:
                temperature, pressure, humidity, altitude = get_temperature_reading()
                readings = {"temperature": temperature, "pressure": pressure,"humidity": humidity, "altitude": altitude}
                
                mqttClient.publish(PUBLISH_TOPIC, ujson.dumps(readings).encode())
                last_publish = current_time
            time.sleep(1)


if __name__ == "__main__":
    while True:
        try:
            main()
        except OSError as e:
            print("Error: " + str(e))
            reset()