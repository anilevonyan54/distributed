from redis import Redis
from rq import Queue
from tasks import send_email

redis_conn = Redis(host='localhost', port=6379)
queue = Queue('emails', connection=redis_conn)

if __name__ == "__main__":
    job = queue.enqueue(
        send_email,
        "recipient@example.com",
        "Distributed Queue Test",
        "This email was sent asynchronously via a worker!"
    )
    print(f"Job submitted! Job ID: {job.id}")
