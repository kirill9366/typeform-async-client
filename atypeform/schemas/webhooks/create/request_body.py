# standart imports
from typing import Optional

# third-party imports
from pydantic import BaseModel


class RequestBodyModel(BaseModel):
    enabled: Optional[bool]
    secret: Optional[str]
    url: Optional[str]
    verify_ssl: Optional[bool]
