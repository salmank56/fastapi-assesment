# FastAPI Snowflake CRUD Project

## Project Overview
This is a FastAPI-based project demonstrating CRUD (Create, Read, Update, Delete) operations integrated with Snowflake using SQLAlchemy.

## Prerequisites
- Python 3.8+
- pip
- Virtual environment support

## Setup Instructions

### 1. Create a Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv
```

### 2. Activate the Virtual Environment

#### On Linux/macOS:
```bash
source venv/bin/activate
```

#### On Windows:
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install project dependencies
pip install -r requirements.txt

# Resolve potential Pydantic email validation issues
pip install 'pydantic[email]'
```

## Troubleshooting

### Pydantic Email Validation
If you encounter issues with Pydantic email validation, ensure you've run:
```bash
pip install 'pydantic[email]'
```

## Additional Notes
- Ensure you have the necessary Snowflake credentials configured
- Check your database connection settings before running the application
