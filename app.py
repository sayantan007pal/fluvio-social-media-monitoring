from flask import Flask, render_template
import asyncio
from order_service import process_order
from inventory_service import update_inventory
from invoice_service import generate_invoice
from notification_service import send_notification
from fluvio import Fluvio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_order', methods=['POST'])
async def process_order_route():
    # Simulate an order and publish it to the 'orders' topic
    order = Order(
        id="order1",
        customer_name="John Doe",
        item="Widget",
        quantity=2
    )
    async with Fluvio.connect() as fluvio:
        await process_order(fluvio, order)

    # Start the microservices
    asyncio.create_task(update_inventory(Fluvio.connect()))
    asyncio.create_task(generate_invoice(Fluvio.connect()))
    asyncio.create_task(send_notification(Fluvio.connect()))

    return "Order processed successfully"

if __name__ == '__main__':
    app.run(debug=True)