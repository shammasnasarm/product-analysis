# Product Analysis Project

A Django REST API project for managing and analyzing product data with filtering capabilities.

## Project Structure

```
├── analysis/           # Django project settings
├── my_app/            # Main application with Product model
├── scripts/           # Utility scripts for data import
│   ├── large_dataset.csv
│   └── product_upload_script.py
├── manage.py          # Django management script
└── requirements.txt   # Python dependencies
```

## Features

- Product management with REST API
- Django REST Framework integration
- Filtering support with django-filter
- Bulk data upload from CSV
- Caching support

## Setup Instructions

### 1. Create Virtual Environment

```bash
python3 -m venv venv
```

### 2. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
python manage.py migrate
```

### 5. Start Development Server

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## Load Data from CSV

To import products from the CSV file, run the following commands:

### 1. Open Django Shell

```bash
python manage.py shell
```

### 2. Import and Run the Upload Script

```python
from scripts import product_upload_script
```

This will automatically load all products from `scripts/large_dataset.csv` into the database.

**Note:** The script processes data in chunks of 1000 records for efficient memory management and automatically handles negative values for price and stock fields.

## API Endpoints

Once the server is running, you can access the following API endpoints:

### Base URL
`http://127.0.0.1:8000/api/`

### Available Endpoints

#### 1. **Product Analytics**
- **URL:** `GET /api/products/analytics/`
- **Description:** Get analytics data for products with aggregated statistics
- **Returns:**
  - Total number of products
  - Average price
  - Total stock value
- **Supports Filters:**
  - `?category=Electronics` - Filter by category
  - `?price_min=10` - Minimum price
  - `?price_max=1000` - Maximum price
- **Example:** `GET /api/products/analytics/?category=Electronics&price_min=100&price_max=500`
- **Note:** Results are cached for 5 minutes for better performance

## Models

### Product
- `name` (CharField): Product name
- `category` (CharField): Product category (indexed)
- `price` (DecimalField): Product price (indexed)
- `stock` (IntegerField): Stock quantity

## Deactivate Virtual Environment

When you're done working:

```bash
deactivate
```

## Technologies Used

- Django 5.2.8
- Django REST Framework 3.16.1
- django-filter 25.2
- pandas 2.3.3
- numpy 2.3.4

## Notes

- The project uses SQLite as the database (suitable for development)
- Caching is enabled with 5-minute timeout
- Price and stock fields are indexed for better query performance
