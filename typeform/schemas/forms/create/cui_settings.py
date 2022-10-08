# standart imports
from typing import Optional

# third-party imports
from pydantic import BaseModel

from typing_extensions import Literal


class CuiSettingsModel(BaseModel):
    avatar: Optional[str]
    is_typing_emulation_disabled: Optional[bool]
    typing_emulation_speed: Optional[Literal["alow", "medium", "fast"]]
