# amqps://csdtcgta:v98deUl30Tiu5a5QckoqZNnjbKmH9VQt@finch.rmq.cloudamqp.com/csdtcgta
import json

import pika

params = pika.URLParameters('amqps://csdtcgta:v98deUl30Tiu5a5QckoqZNnjbKmH9VQt@finch.rmq.cloudamqp.com/csdtcgta')

connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
