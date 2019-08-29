#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes
import datetime
from pytz import timezone
import random

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):
	
	liste_reponses = ["Je suis ravie"]
	sentence = liste_reponses[random.randint(0,len(liste_reponses)-1)]
	lieu = intent_message.slots.Lieu.first().value
	sentence += lieu
	hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
