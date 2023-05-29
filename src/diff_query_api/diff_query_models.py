from typing import Optional, List, Tuple
from pydantic import BaseModel
from enum import StrEnum
from diff_query_api.constants import DEFAULT_QUERY_TEXT

class EventTypeEnum(StrEnum):
    REQUEST = "REQUEST"
    RESPONSE = "RESPONSE"

class DiffQueryGetDiffRequest(BaseModel):
    primaryText: str
    secondaryText: str
    
class DiffQueryGetDiffResponse(BaseModel):
    textDiff: List[Tuple[int, str]]

class DiffQueryCallModelRequest(BaseModel):
    textDiff: str
    query: Optional[str] = DEFAULT_QUERY_TEXT

class DiffQueryCallModelResponse(BaseModel):
    modelResponse = str