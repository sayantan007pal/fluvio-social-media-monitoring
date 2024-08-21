from fluvio import Fluvio
from order_service import Order

async def update_inventory(fluvio: Fluvio):
    consumer = fluvio.consumer().topic("orders").build()

    async for message in consumer:
        order: Order = message.value()
        # Update the inventory based on the order
        print(f"Updated inventory for item: {order.item}")