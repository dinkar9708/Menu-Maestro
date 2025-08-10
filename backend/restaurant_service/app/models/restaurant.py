from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from database import Base

class RestaurantModel(Base):
    __tablename__ = "restaurants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    owner_id = Column(UUID(as_uuid=True), nullable=False)
    # owner = relationship("User", back_populates="restaurants")





