# standart imports
from typing import Optional

# third-party imports
from pydantic import BaseModel


class VariablesModel(BaseModel):
    price: Optional[float]
    score: Optional[int]
