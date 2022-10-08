# standart imports
from typing import Optional

# third-party imports
from pydantic import BaseModel
from pydantic import Field

from typing_extensions import Literal


class PropertiesModel(BaseModel):
    description: Optional[str]
    show_button: Optional[str]
    button_text: Optional[str]


class AttachmentPropertiesModel(BaseModel):
    description: Optional[str]


class AttachmentModel(BaseModel):
    type_: Optional[str] = Field(alias="type")
    href: Optional[str]
    scale: Optional[Literal[
        0.4,
        0.6,
        0.8,
        1,
    ]]
    properties: Optional[AttachmentPropertiesModel]


class LayoutModel(BaseModel):
    type_: Optional[str] = Field(alias="type")
    placement: Optional[Literal[
        "left",
        "right",
    ]]
    attachment: Optional[AttachmentModel]


class WelcomeScreenModel(BaseModel):
    ref: Optional[str]
    title: str
    properties: Optional[PropertiesModel]
    attachment: Optional[AttachmentModel]
    layout: Optional[LayoutModel]
