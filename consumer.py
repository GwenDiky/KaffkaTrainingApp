from kafka import KafkaConsumer

consumer = KafkaConsumer(
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=False,
                         value_deserializer=lambda v: v.decode('utf-8')
                         )

consumer.subscribe(topics=['topic'])


def displayMessages():
    msg = consumer.poll(timeout_ms=100)
    if msg:
        for topic, partition, offset, key, value in msg.items():
            print(f"Topic: {topic}\n"
                  f"Partition: {partition}\n"
                  f"Offset: {offset}\n"
                  f"Key: {key}\n"
                  f"Value: {value}")