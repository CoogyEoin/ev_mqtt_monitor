from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


class AWSMQTTHandler:

    def __init__(self, endpoint, mqtt_uplink_topic, mqtt_downlink_topic, certificate, root_ca, private_key, client_id):
        """
        MQTTHandler class
        This class is used for connecting to the AWS IoT core service an
        and handling the uplink and downlink messages from the serer.
        ---Arguments---
        """
        self.the_endpoint = endpoint
        self.the_mqtt_uplink_topic = mqtt_uplink_topic
        self.the_mqtt_downlink_topic = mqtt_downlink_topic
        self.client = None
        self.the_root_ca = root_ca
        self.the_certificate = certificate
        self.the_private_key = private_key
        self.the_client_id = client_id
        self.mqtt_setup()

    def mqtt_setup(self):
        """
        Method used to initialize the AWS client with the CA and private key.
        """
        self.client = AWSIoTMQTTClient(self.the_client_id)
        self.client.configureEndpoint(self.the_endpoint, 8883)
        self.client.configureCredentials(self.the_root_ca, self.the_private_key, self.the_certificate)
        self.client.configureAutoReconnectBackoffTime(1, 32, 20)
        self.client.configureOfflinePublishQueueing(-1)
        self.client.configureDrainingFrequency(2)
        self.client.configureConnectDisconnectTimeout(10)
        self.client.configureMQTTOperationTimeout(5)
        self.client.connect()
        self.client.subscribe(self.the_mqtt_downlink_topic, 1, on_message)

    def publish_mqtt_message(self, message):
        """
		Method for publishing messages to the MQTT uplink topic.
		
		---Arguments---
		message: The message being sent to the MQTT topic
		"""
        self.client.publish(self.the_mqtt_uplink_topic, message, 1)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
