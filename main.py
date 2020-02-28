from handlers.aws_mqtt_handler import AWSMQTTHandler
from handlers.data_handler import DataHandler
import time
import json
import argparse

dataMap = None

with open('config.json') as f:
    # use safe_load instead load
    dataMap = json.load(f)

# Read in command-line parameters
parser = argparse.ArgumentParser()

parser.add_argument("-r", "--rootCA", action="store", required=True, dest="rootCAPath", help="Root CA file path")
parser.add_argument("-c", "--cert", action="store",required=True, dest="certificatePath", help="Certificate file path")
parser.add_argument("-k", "--key", action="store",required=True, dest="privateKeyPath", help="Private key file path")

args = parser.parse_args()
rootCAPath = args.rootCAPath
certificatePath = args.certificatePath
privateKeyPath = args.privateKeyPath
endpoint = dataMap["server"]
uplink = dataMap["uplink_topic"]
downlink = dataMap["downlink_topic"]
clientID = dataMap["clientID"]

def main():
    print("Dia duit")

    input_pin = 13
    output_pin = 15

    mqtt = AWSMQTTHandler(endpoint, uplink, downlink, certificatePath,rootCAPath, privateKeyPath, clientID)
    data = DataHandler(input_pin,output_pin)

    while(True):
        time.sleep(5)
        msg = data.get_mqtt_message()
        
        print("Sending message: " + msg)
        mqtt.publish_mqtt_message(msg)

if __name__ == "__main__":
    main()
