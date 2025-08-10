from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    role_name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class UserRole(Base):
    __tablename__ = "user_roles"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), index=True)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.role_id"), index=True)
    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'role_id'),
    )
    created_at = Column(DateTime, default=datetime.utcnow)

    role = relationship("Role", backref="user_roles")
    user = relationship("User", backref="user_roles")


class RolePermissions(Base):
    __tablename__ = "role_permissions"

    role_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    permission_id = Column(UUID(as_uuid=True), ForeignKey("permissions.permission_id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    permission = relationship("Permission", backref="roles")

class Permission(Base):
    __tablename__ = "permissions"

    permission_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    permission_name = Column(String, unique=True, index=True, nullable=False)
