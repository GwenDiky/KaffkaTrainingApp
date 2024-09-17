from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
)
producer.send("topic", value="I'm sending my greetings with love to WhiteSnake! 🐍".encode("utf-8"))
producer.flush()