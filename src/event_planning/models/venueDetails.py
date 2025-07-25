from pydantic import BaseModel, Field

# Define a Pydantic model for venue details 
# (demonstrating Output as Pydantic)
class VenueDetails(BaseModel):
    name: str = Field(description="Name of the venue")
    address: str = Field(description="Full address of the venue")
    capacity: int = Field(description="Maximum capacity of the venue")
    booking_status: str = Field(description="Current booking status of the venue")