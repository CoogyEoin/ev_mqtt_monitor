import paho.mqtt.client as mqtt

class MQTTHandler:

	def __init__(self, mqtt_server, mqtt_uplink_topic, mqtt_downlink_topic):
		self.the_mqtt_server = mqtt_server
		self.the_mqtt_uplink_topic = mqtt_uplink_topic
		self.the_mqtt_downlink_topic = mqtt_downlink_topic
		self.client = mqtt.Client()
		self.mqtt_setup()

	def mqtt_setup(self):
		self.client.on_connect = self.connect_callback()
		self.client.on_message = on_message
		self.client.connect(self.the_mqtt_server, 1883, 60)


	def publish_mqtt_message(self, message):
		self.client.publish(self.the_mqtt_uplink_topic, message)
		print("Publishing MQTT message: " + message)

	def connect_callback(self):
		print("Connected to MQTT server")

		# Subscribing in on_connect() means that if we lose the connection and
		# reconnect then subscriptions will be renewed.
		self.client.subscribe(self.the_mqtt_downlink_topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))