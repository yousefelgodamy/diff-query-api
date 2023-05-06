from typing import Optional
from pydantic import BaseModel
from diff_query_api.constants import DEFAULT_QUERY_TEXT


class DiffQueryRequest(BaseModel):
    primaryText: str
    secondaryText: str
    query: Optional[str] = DEFAULT_QUERY_TEXT
    

class DiffQueryResponse(BaseModel):
    diff: str
    modelResponse: str
