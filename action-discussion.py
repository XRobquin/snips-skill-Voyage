#!/usr/bin/env python2
from hermes_python.hermes import Hermes
import datetime
from pytz import timezone
import random

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):
	sentence = "Fantastique"
	hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
