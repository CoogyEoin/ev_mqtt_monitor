import json
import datetime
#import RPi.GPIO as GPIO

class DataHandler:
    
    def __init__(self, input_pin, output_pin):
        """
        DataHandler class
        This class is used for returning and processing the required messages
        for the MQTT devices
        ---Arguments---
        input_pin: The GPIO pin on the Raspberry Pi for getting the input
        output_pin: The GPIO pin on the Raspberry Pi for getting the output

        """
        self.input_pin = input_pin
        self.output_pin = output_pin
        self.power_value = 0
        self.shortage_value = 0
        self.json_message = self.get_json()
        
        
    def get_json(self):
        """
        Returns the JSON containing the power, timestamp and 
        the cable shortage status.
        """
        return {
                "power": self.get_power(), 
                "timestamp": self.get_timestamp(), 
                "shortage": self.get_shortage()
                }
        
    def get_mqtt_message(self):
        """
        Returns a valid JSON string of the relevant values
        so it can be sent over MQTT.
        """
        return json.dumps(self.get_json(), default=self.converter_callback)
    
    
    def get_power(self):
        """
        This method is used for getting the power
        value from the GPIO pins. It is not yet clear
        how this is going to be obtained so for now it's just a
        constant value.
        """
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(self.input_pin, GPIO.IN)
        return 0
        
        
        
    def get_timestamp(self):
        """
        Returns the datetime for the MQTT message.
        UTC convention may not be suitable when in the cloud.
        """
        return datetime.datetime.utcnow()
        
        
    def get_shortage(self):
        """
        Returns the status for the cable shortage.
        Used to diagnose cable health and notify when
        the cable experiences deterioration.
        """
        return 0
    
    def converter_callback(self, value):
        """
        Callback function used to convert datetime datatypes
        to JSON serialable strings.
        """
        if isinstance(value, datetime.datetime):
            return value.__str__()
        

