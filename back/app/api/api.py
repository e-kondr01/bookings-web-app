from fastapi import APIRouter

from app.api.endpoints import bookings, hotels

api_router = APIRouter()
api_router.include_router(hotels.router, prefix="/hotels", tags=["Отели"])
api_router.include_router(bookings.router, prefix="/bookings", tags=["Бронирования"])
