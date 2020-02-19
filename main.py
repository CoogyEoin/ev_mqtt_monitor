from handlers.mqtt_handler import MQTTHandler

import time
import yaml

dataMap = None

with open('config.yaml') as f:
    # use safe_load instead load
    dataMap = yaml.safe_load(f)


def main():
    print("Dia duit")

    server = dataMap['mqtt']['server']
    uplink =  dataMap['mqtt']['uplink_topic']
    downlink = dataMap['mqtt']['downlink_topic']

    mqtt = MQTTHandler(server, uplink, downlink)

    while(True):
        time.sleep(5)
        mqtt.publish_mqtt_message("Dia duit")

if __name__ == "__main__":
    main()
