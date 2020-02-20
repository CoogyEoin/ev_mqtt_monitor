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
    
    input_pin = 13
    output_pin = 15

    mqtt = MQTTHandler(server, uplink, downlink)
    data = DataHandler(input_pin,output_pin)

    while(True):
        time.sleep(5)
        msg = data.get_mqtt_message()
        
        print("Sending message: " + msg)
        mqtt.publish_mqtt_message(msg)

if __name__ == "__main__":
    main()
