import json, os, django

import pika

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MicroservicesBackend.settings")
django.setup()

from products.models import Products

params = pika.URLParameters('amqps://csdtcgta:v98deUl30Tiu5a5QckoqZNnjbKmH9VQt@finch.rmq.cloudamqp.com/csdtcgta')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(channel, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    product = Products.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product Likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')
channel.start_consuming()
channel.close()
