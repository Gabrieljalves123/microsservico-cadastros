
import json
import os
import pika


def publicar_agendamento(evento: dict):
    conexao = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST", "localhost")
        )
    )

    try:
        canal = conexao.channel()

        canal.queue_declare(
            queue="agendamentos_criados",
            durable=True
        )

        canal.basic_publish(
            exchange="",
            routing_key="agendamentos_criados",
            body=json.dumps(evento, default=str).encode("utf-8"),
            properties=pika.BasicProperties(
                delivery_mode=2,
                content_type="application/json"
            )
        )
    finally:
        conexao.close()
