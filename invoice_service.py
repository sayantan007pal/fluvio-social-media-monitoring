from fluvio import Fluvio
from order_service import Order

async def generate_invoice(fluvio: Fluvio):
    consumer = fluvio.consumer().topic("orders").build()

    async for message in consumer:
        order: Order = message.value()
        # Generate an invoice for the order
        print(f"Generated invoice for order: {order.id}")