# standart imports
from typing import Optional

# third-party imports
from pydantic import BaseModel


class WorkSpaceModel(BaseModel):
    href: Optional[str]
