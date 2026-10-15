import pika
import json

def publicar_evento_cadastro(cliente_data: dict):
    # Conexão ao RabbitMQ local que levantámos no Docker
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    # Declara a fila Point-to-Point (Fila Simples)
    channel.queue_declare(queue='fila_cadastro_clientes', durable=True)
    
    # Publica a mensagem serializada em JSON
    channel.basic_publish(
        exchange='',
        routing_key='fila_cadastro_clientes',
        body=json.dumps(cliente_data),
        properties=pika.BasicProperties(
            delivery_mode=2,  # Torna a mensagem persistente
        )
    )
    connection.close()