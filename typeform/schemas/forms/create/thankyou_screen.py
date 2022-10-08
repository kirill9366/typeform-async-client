# standart imports
from typing import Optional

# third-party imports
from pydantic import BaseModel
from pydantic import Field

from typing_extensions import Literal


class PropertiesModel(BaseModel):
    show_button: Optional[bool]
    button_text: Optional[str]
    button_mode: Optional[Literal[
        "reload",
        "default_redirect",
        "redirect",
    ]]
    redirect_url: Optional[str]
    share_icons: Optional[bool]


class FocalPointModel(BaseModel):
    x: Optional[float]
    y: Optional[float]


class AttachmentPropertiesModel(BaseModel):
    brightness: Optional[float]
    description: Optional[str]
    focal_point: Optional[FocalPointModel]


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


class ThankYouScreenModel(BaseModel):
    ref: Optional[str]
    title: str
    type_: Optional[str] = Field(alias="type")
    properties: Optional[PropertiesModel]
    attachment: Optional[AttachmentModel]
    layout: Optional[LayoutModel]
