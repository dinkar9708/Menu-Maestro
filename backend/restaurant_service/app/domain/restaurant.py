from pydantic import BaseModel

# --- Domain Entity ---
class Restaurant:
    def __init__(self, id, name, address, phone_number, email, created_at, is_active, owner_id):
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.created_at = created_at
        self.is_active = is_active
        self.owner_id = owner_id