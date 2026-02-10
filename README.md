# Home-serives

# UrbanClap-Style Home Services Platform (Mini Sprint)

A mini UrbanClap-style web application built using **FastAPI** (backend) and **React** (frontend).  
This project focuses on the **Customer Flow**: browsing services and creating bookings.  

---

## **Project Overview**

This application simulates a home services platform where customers can:

- Browse available services
- Create a booking for a selected service
- See booking confirmation

**Note:** This project **does not include** authentication, payment, provider onboarding, or admin dashboard. It is a focused mini-sprint on customer experience.

---

## **Tech Stack**

### Backend
- Python 3.12
- FastAPI
- SQLAlchemy ORM + Alembic (PostgreSQL)
- UUID primary keys
- Pydantic schemas for validation
- Layered architecture with routers, models, schemas
- Auto-create customers from `X-Customer-Id` header
- Seed script for services

### Frontend
- React (functional components & hooks)
- Axios for API calls
- Mock authentication with UUID in `localStorage`
- Dynamic rendering of services & bookings
- Clean modern UI (colors & fonts based on design spec)

---

## **Database Models**

### Customer
| Column      | Type   | Notes                |
|------------|--------|--------------------|
| id         | UUID   | Primary Key         |
| name       | String | Nullable            |
| phone      | String | Nullable            |
| created_at | Timestamp | Auto-generated     |

### Service
| Column      | Type   | Notes                |
|------------|--------|--------------------|
| id         | UUID   | Primary Key         |
| name       | String | Required            |
| description| String | Required            |
| price      | Integer| Required            |
| created_at | Timestamp | Auto-generated     |

NOte:In service we are just add the only Three serivce

### Booking
| Column       | Type   | Notes                                |
|-------------|--------|--------------------------------------|
| id          | UUID   | Primary Key                           |
| customer_id | UUID   | Foreign Key → Customer                |
| service_id  | UUID   | Foreign Key → Service                 |
| booking_time| Timestamp | Optional, defaults to now           |
| address     | String | Required                               |
| status      | String | Default: CREATED                       |
| created_at  | Timestamp | Auto-generated                        |

---

## **How to Run the Project**

### Backend
py -m pip install -r requirements.txt

# data base
# .env
DATABASE_URL=postgresql://username:password@localhost:5432/home_services

# Run Alembic migrations:
alembic upgrade head

# seed data (dummy data add for services)
# Seed the database with initial services:

py seed.py

# Start backend server:
py -m uvicorn app.main:app --reload


### Frontend

#Navigate to frontend folder
cd frontend

# Install dependencies
npm install

# Start frontend
npm start
