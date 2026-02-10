from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import services, bookings

app = FastAPI(title="UrbanClap Home Services")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(services.router)
app.include_router(bookings.router)
