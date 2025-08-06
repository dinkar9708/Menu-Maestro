from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from models.restaurant import RestaurantModel
from domain.restaurant import Restaurant
from crud.restaurant_repository import RestaurantRepository

class RestaurantRepoSQLAlchemy(RestaurantRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, restaurant: Restaurant):
        model = RestaurantModel(
            id=restaurant.id,
            name=restaurant.name,
            address=restaurant.address,
            phone_number=restaurant.phone_number,
            email=restaurant.email,
            created_at=restaurant.created_at,
            is_active=restaurant.is_active,
            owner_id=restaurant.owner_id
        )
        self.session.add(model)
        await self.session.commit()
        return restaurant

    async def find_by_id(self, restaurant_id) -> Optional[Restaurant]:
        result = await self.session.execute(select(RestaurantModel).filter_by(id=restaurant_id))
        model = result.scalars().first()
        if model:
            return Restaurant(
                model.id, model.name, model.address, model.phone_number,
                model.email, model.created_at, model.is_active, model.owner_id
            )
        return None

    async def find_by_owner(self, owner_id) -> List[Restaurant]:
        result = await self.session.execute(select(RestaurantModel).filter_by(owner_id=owner_id))
        models = result.scalars().all()
        return [
            Restaurant(m.id, m.name, m.address, m.phone_number,
                       m.email, m.created_at, m.is_active, m.owner_id)
            for m in models
        ]