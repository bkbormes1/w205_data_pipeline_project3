#!/usr/bin/env python
import json
from kafka import KafkaProducer
from flask import Flask, request

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:29092')


def log_to_kafka(topic, event):
    event.update(request.headers)
    producer.send(topic, json.dumps(event).encode())


@app.route("/")
def default_response():
    # need to input GET API to pull games JSON
    default_event = {'event_type': 'default'}
    log_to_kafka('games', default_event)
    return "Game logged!\n"


# @app.route("/purchase_a_sword")
#def purchase_a_sword():
#    purchase_sword_event = {'event_type': 'purchase_sword'}
#    log_to_kafka('events', purchase_sword_event)
#    return "Sword Purchased!\n"