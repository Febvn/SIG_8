from pydantic import BaseModel, Field
from typing import Optional

class FasilitasCreate(BaseModel):
    nama: str = Field(..., min_length=3)
    jenis: str
    alamat: Optional[str] = None
    longitude: float = Field(..., ge=105, le=106) # Adjusted for Lampung area as per tip
    latitude: float = Field(..., ge=-6, le=-5)
