from os import environ as env
import datetime

import faust


class RawMessage(faust.Record):
    text: str


class ParsedMessage(faust.Record):
    text: str
    timestamp: str


def now():
    return str(datetime.datetime.now())


app_name = env.get('FAUST_APP_NAME', 'sample')
app_kafka_broker = env.get('FAUST_KAFKA_BROKER', 'kafka://kafka-broker:9092')
app_store = env.get('FAUST_STORE', 'memory://')
app_recv_topic_name = env.get('FAUST_RECV_TOPIC', 'org.fedoraproject.prod.techtalk.message')
app_send_topic_name = env.get('FAUST_SEND_TOPIC', 'org.fedoraproject.prod.techtalk.message.parsed'
        )
app = faust.App(app_name, broker=app_kafka_broker, store=app_store)

recv_topic = app.topic(app_recv_topic_name, value_type=RawMessage)
send_topic = app.topic(app_send_topic_name, value_type=ParsedMessage)


@app.agent(recv_topic)
async def handler_recv(stream):
    async for message in stream:
        print(f'Received Message: {message.text}')
        await send_topic.send(value=ParsedMessage(message.text, now()))


@app.agent(send_topic)
async def handler_send(stream):
    async for message in stream:
        print(f'Received Parsed Message: {message.text}:{message.timestamp}')
