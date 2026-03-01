# Inventory Service API

A professional RESTful API developed with Django and Django REST Framework, designed for efficient inventory management in corporate environments. The system features centralized product management, stock movements, and role-based access control for multi-tenant organizations.

## Key Features

- Multi-tenant Architecture: Support for multiple companies with complete data isolation.
- Product Management: Detailed tracking of names, SKUs, descriptions, and stock levels.
- Inventory Control: Automated system to record stock entries (IN), exits (OUT), and manual adjustments with stock level validation.
- Critical Stock Levels: Preventive monitoring of minimum stock levels to avoid shortages.
- Security and RBAC: Robust access control based on roles (Owner, Admin, Manager, Employee).
- Traceability: Historical log of which user performed what modification and when.
- Scalable Identifiers: Use of UUIDs for all primary entities to enhance security and scalability.

## Tech Stack

- Language: Python 3.x
- Web Framework: Django 5.x
- API Toolkit: Django REST Framework (DRF)
- Database: PostgreSQL (via Psycopg3)
- Configuration: Django Environ and Python Dotenv
- Environment Management: Pip (requirements.txt)

## Project Structure

The project is organized into modular applications following Django's best practices:

- apps.users: Custom user management and role hierarchy.
- apps.companies: Business entity management (Tenants).
- apps.inventory: Core logic for products and warehouse movements.
- config: Global project setup and API configuration.

## Prerequisites

- Python 3.10 or higher.
- PostgreSQL database.
- Virtual environment (recommended).

## Installation & Setup

Follow these steps to get the service running locally:

1. Clone the repository:
   git clone https://github.com/your-username/inventory-service-api.git
   cd inventory-service-api

2. Create and activate a virtual environment:
   python -m venv env

   # On Windows

   .\env\Scripts\activate

   # On Linux/Mac

   source env/bin/activate

3. Install required dependencies:
   pip install -r requirements.txt

4. Configure environment variables:
   Create a .env file in the project root and define the following values:

   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=postgres://user:password@localhost:5432/db_name

5. Run database migrations:
   python manage.py migrate

6. Start the development server:
   python manage.py runserver

## Environment Variables

The project requires the following environment variables in your .env file:

- SECRET_KEY: Security key for the Django instance.
- DEBUG: Boolean value (True/False) for debug mode.
- ALLOWED_HOSTS: Comma-separated list of allowed hostnames.
- DATABASE_URL: Standard database connection string (psql://user:pass@host:port/dbname).

## Contributing

If you'd like to contribute:

1. Fork the repository.
2. Create a new feature branch (git checkout -b feature/awesome-feature).
3. Commit your changes (git commit -m 'Add awesome feature').
4. Push to the branch (git push origin feature/awesome-feature).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
