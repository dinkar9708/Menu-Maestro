from uuid import uuid4
from datetime import datetime
from domain.restaurant import Restaurant
from dto.restaurant_dto import RestaurantDTO

# --- Factory for Restaurant ---
class RestaurantFactory:
    @staticmethod
    def create(dto: RestaurantDTO, owner_id) -> Restaurant:
        return Restaurant(
            id=uuid4(),
            name=dto.name.strip(),
            address=dto.address.strip(),
            phone_number=dto.phone_number,
            email=dto.email.strip(),
            created_at=datetime.utcnow(),
            is_active=True,
            owner_id=owner_id
        )
