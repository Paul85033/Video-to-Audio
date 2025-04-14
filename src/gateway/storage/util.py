import pika, json


def upload(f, fs, channel, access):
    try:
        print("Uploading file to GridFS...")
        fid = fs.put(f)
        print(f"Stored file with id: {fid}")
    except Exception as err:
        print("GridFS error:", err)
        return "internal server error", 500

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    try:
        print("Declaring queue...")
        channel.queue_declare(queue="video", durable=True)
        print("Publishing to RabbitMQ...")
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
        print("Publish successful.")
    except Exception as err:
        print("RabbitMQ error:", err)
        fs.delete(fid)
        return "internal server error", 500
