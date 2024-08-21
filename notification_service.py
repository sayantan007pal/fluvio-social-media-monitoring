from fluvio import Fluvio
from order_service import Order

async def send_notification(fluvio: Fluvio):
    consumer = fluvio.consumer().topic("orders").build()

    async for message in consumer:
        order: Order = message.value()
        # Send a notification to the customer
        print(f"Sent notification to {order.customer_name}")