from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SummaryRequest(BaseModel):
    content: str
    mode: Optional[str] = "brief"  # options: brief, detailed, bullet

class SummaryResponse(BaseModel):
    summary: str

class HistoryResponse(BaseModel):
    id: str
    timestamp: datetime
    mode: str
    summary: str
    original_excerpt: str
