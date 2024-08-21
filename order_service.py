from fluvio import Fluvio
from serde import Serialize, Deserialize

@Serialize
@Deserialize
class Order:
    id: str
    customer_name: str
    item: str
    quantity: int

async def process_order(fluvio: Fluvio, order: Order):
    # Process the order
    print(f"Received order: {order}")

    # Publish the order to the 'orders' topic
    await fluvio.producer().send_key("orders", order.id.encode(), order)
    print("Order published to the 'orders' topic.")