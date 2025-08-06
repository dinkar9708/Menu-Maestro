from typing import List, Optional
from crud.restaurant_repository import RestaurantRepository
from domain.restaurant import Restaurant
from dto.restaurant_dto import RestaurantDTO
from factories.restaurant_factory import RestaurantFactory

class RestaurantService:
    def __init__(self, repo: RestaurantRepository):
        self.repo = repo

    async def create_restaurant(self, dto: RestaurantDTO, owner_id) -> Restaurant:
        restaurant = RestaurantFactory.create(dto, owner_id)
        return await self.repo.save(restaurant)

    async def get_restaurant_by_id(self, restaurant_id) -> Optional[Restaurant]:
        return await self.repo.find_by_id(restaurant_id)

    async def get_restaurants_by_owner(self, owner_id) -> List[Restaurant]:
        return await self.repo.find_by_owner(owner_id)