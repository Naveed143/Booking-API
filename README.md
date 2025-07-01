# Fitness Booking API

A lightweight FastAPI-based backend to view and book fitness classes, with timezone support and email-based booking lookup.

---

## Tech Stack

- **Python 3.10+**
- **FastAPI** – for building REST APIs
- **Pydantic** – data validation
- **Uvicorn** – ASGI server for running FastAPI
- **pytz** – for timezone conversion
- **UUID** – for generating booking IDs
- **Pytest** – for testing

---

## Install Dependencies

Use this command to install all required packages:

```bash
pip install fastapi uvicorn pydantic pytz pytest
```

## Run the App
```bash
uvicorn main:app --reload
```

## Open in the Browser
Swagger Docs: http://localhost:8000/docs

## Run tests
```bash
pytest test_main.py
```

## API Endpoints
1. Root – Welcome Message
```bash
curl -X GET http://localhost:8000/
```

2. Get All Classes
```bash
curl -X GET "http://localhost:8000/classes?timezone=Asia/Kolkata"
```

3. Book a Class
```bash
curl -X POST http://localhost:8000/book \
  -H "Content-Type: application/json" \
  -d '{"class_id": "1", "client_name": "John Doe", "client_email": "john@example.com"}'
```

4. Get Bookings by Email
```bash
curl -X GET "http://localhost:8000/bookings?client_email=john@example.com"
```
