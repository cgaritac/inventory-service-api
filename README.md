# Inventory Service API

A robust, enterprise-ready RESTful API built with **Django 5.2** and **Django REST Framework**. This service is designed to manage complex inventory systems for multi-tenant organizations, featuring centralized product management, real-time stock movements, and strict data isolation.

## Key Features

- **Multi-tenant Architecture**: Inherently multi-tenant with data isolation at the database level using a `Company` owner pattern.
- **Product Management**: Lifecycle tracking of products including SKUs, descriptions, and real-time stock levels.
- **Dynamic Inventory Control**:
  - Automated stock synchronization on every movement (`IN`, `OUT`, `ADJUSTMENT`).
  - Validation rules to prevent negative stock (insufficient stock errors).
- **Advanced Security (RBAC)**:
  - Role-based access control: `Owner`, `Admin`, `Manager`, `Employee`.
  - Permission-based viewsets ensuring users only see data belonging to their company.
- **JWT Authentication**: Secure stateless authentication using Simple JWT (JSON Web Tokens).
- **Traceability**: Audit-ready tracking with `created_by`, `updated_by`, and timestamp fields for all movements.
- **Enterprise Standards**:
  - UUID primary keys for all entities to prevent ID enumeration.
  - Scalable indexes for high-performance querying on SKUs and Companies.

## Tech Stack

- **Framework**: [Django 5.2+](https://www.djangoproject.com/)
- **API Toolkit**: [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
- **Authentication**: [DRF Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
- **Database**: [PostgreSQL](https://www.postgresql.org/) (via `psycopg3`)
- **Environment**: `python-dotenv` & `django-environ`
- **Language**: Python 3.10+

## Project Structure

The project follows a modular architecture:

- `apps.users`: Custom user model with organizational roles.
- `apps.companies`: Logical grouping of data (Tenants).
- `apps.inventory`: Core logic for `Product` and `InventoryMovement`.
- `config`: Global settings, JWT configurations, and root URL routing.

## API Endpoints

### Authentication

| Method | Endpoint              | Description                          |
| ------ | --------------------- | ------------------------------------ |
| POST   | `/api/token/`         | Obtain Access and Refresh JWT tokens |
| POST   | `/api/token/refresh/` | Refresh expired access tokens        |

### Inventory (Requires Authentication)

| Method               | Endpoint               | Description                               |
| -------------------- | ---------------------- | ----------------------------------------- |
| GET/POST             | `/api/products/`       | List and create products for your company |
| GET/PUT/PATCH/DELETE | `/api/products/{id}/`  | Manage a specific product                 |
| GET/POST             | `/api/movements/`      | List and record stock movements           |
| GET                  | `/api/movements/{id}/` | View details of a specific movement       |

> **Note**: Users are automatically filtered to only see data from the `Company` associated with their profile.

## Installation & Setup

### 1. Prerequisites

- Python 3.10 or higher.
- PostgreSQL 14+ database.
- Git.

### 2. Clone and Environment

```bash
git clone https://github.com/your-username/inventory-service-api.git
cd inventory-service-api

# Create Virtual Environment
python -m venv env
source env/bin/activate  # On Windows use: .\env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file in the root directory:

```env
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@localhost:5432/inventory_db
```

### 5. Database Initialization

```bash
python manage.py makemigrations
python manage.py migrate

# Create the initial administrative user
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

## Authentication Flow

1. **Login**: Send a `POST` request to `/api/token/` with `username` and `password`.
2. **Access Data**: Include the received access token in the `Authorization` header for all protected requests:
   ```http
   Authorization: Bearer <your_access_token>
   ```
3. **Refresh**: Use the refresh token at `/api/token/refresh/` once the access token expires (default: 30 minutes).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
