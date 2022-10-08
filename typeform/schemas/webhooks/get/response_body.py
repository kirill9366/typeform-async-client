# standart imports
from typing import List
from typing import Optional

# third-party imports
from pydantic import BaseModel
from pydantic import Field


class ItemModel(BaseModel):
    created_at: Optional[str]
    enabled: Optional[bool]
    form_id: Optional[str]
    id_: Optional[str] = Field(alias="id")
    secret: Optional[str]
    tag: Optional[str]
    updated_at: Optional[str]
    url: Optional[str]
    verify_ssl: Optional[bool]


class ResponseBodyModel(BaseModel):
    items: Optional[List[ItemModel]]
