from fastapi import APIRouter, Depends
from uuid import UUID
from dto.restaurant_dto import RestaurantCreate, RestaurantDTO
from services.restaurant_service import RestaurantService
from dto.restaurant_dto import RestaurantResponse
from domain.restaurant import Restaurant
from dependencies.db import get_restaurant_service
from dependencies.auth import get_current_user_id

router = APIRouter()

@router.post("/restaurants", response_model=RestaurantResponse)
async def create_restaurant(dto: RestaurantCreate, owner_id: UUID = Depends(get_current_user_id), service: RestaurantService = Depends(get_restaurant_service)):
    return await service.create_restaurant(dto, owner_id)

@router.get("/restaurants/{restaurant_id}", response_model=RestaurantResponse)
async def get_restaurant(restaurant_id: UUID, service: RestaurantService = Depends(get_restaurant_service)):
    return await service.get_restaurant_by_id(restaurant_id)

@router.get("/owners/me/restaurants", response_model=list[RestaurantResponse])
async def get_restaurants_by_owner(owner_id: UUID = Depends(get_current_user_id), service: RestaurantService = Depends(get_restaurant_service)):
    return await service.get_restaurants_by_owner(owner_id)