from typing import List, Optional
from domain.restaurant import Restaurant

class RestaurantRepository:
    async def save(self, restaurant: Restaurant):
        raise NotImplementedError

    async def find_by_id(self, restaurant_id) -> Optional[Restaurant]:
        raise NotImplementedError

    async def find_by_owner(self, owner_id) -> List[Restaurant]:
        raise NotImplementedError
