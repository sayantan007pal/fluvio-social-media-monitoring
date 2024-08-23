# E-commerce Order Processing Pipeline

## Overview

This project implements a serverless, event-driven e-commerce order processing pipeline using Flask and Fluvio. It demonstrates how to create a microservices architecture for handling various aspects of e-commerce operations, including order processing, inventory management, invoice generation, and customer notifications.

## Features

- Simulates an e-commerce order stream
- Processes orders and publishes them to a Fluvio topic
- Updates inventory based on incoming orders
- Generates invoices for processed orders
- Sends notifications to customers
- Provides a web interface for monitoring the order processing pipeline
- Demonstrates scalability and resilience of a Fluvio-based microservices system

## Prerequisites

- Python 3.7+
- Flask
- Fluvio
- Rust (for Fluvio)

## Installation

1. Clone the repository:

       git clone https://github.com/sayantanpal100/e-commerce-pipeline.git
       cd e-commerce-pipeline

3. Install the required Python packages:

       pip install -r requirements.txt

4. Install Fluvio:

       cargo install fluvio

4. Start the Fluvio cluster:

       fluvio cluster start

## Project Structure


e-commerce-app/
├── app.py
├── order_service.py
├── inventory_service.py
├── invoice_service.py
├── notification_service.py
├── templates/
│   └── index.html
├── static/
│   └── css/
│       └── style.css
└── requirements.txt

## Usage

1. Run the Flask application:

       python app.py

2. Open your web browser and navigate to http://localhost:5000.

3. Use the web interface to simulate order processing and observe the pipeline in action.

## Microservices

### Order Service
Processes incoming orders and publishes them to the Fluvio 'orders' topic.

### Inventory Service
Subscribes to the 'orders' topic and updates the inventory based on processed orders.

### Invoice Service
Generates invoices for processed orders.

### Notification Service
Sends notifications to customers about their order status.

## Scalability and Resilience

This project demonstrates the scalability and resilience of a Fluvio-based microservices system:

- Each microservice can be scaled independently to handle increased load.
- The event-driven architecture allows for loose coupling between services.
- Fluvio provides fault-tolerance and data persistence, ensuring no data loss in case of service failures.

## Customization

You can extend this project by:

- Adding more microservices for additional e-commerce functionalities.
- Implementing real-time analytics on the order data.
- Enhancing the web interface with more detailed reporting and visualizations.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Fluvio](https://www.fluvio.io/)
- [Rust](https://www.rust-lang.org/)
