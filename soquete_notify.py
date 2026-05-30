import argparse
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST", "192.168.1.135")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC = "soquete/notify"

def send_notification(message: str) -> None:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(MQTT_HOST, MQTT_PORT)
    client.publish(TOPIC, message)
    client.disconnect()

parser = argparse.ArgumentParser()
parser.add_argument("--message", required=True, help="Notificación a enviar al cliente soquete")
args = parser.parse_args()

send_notification(args.message)
