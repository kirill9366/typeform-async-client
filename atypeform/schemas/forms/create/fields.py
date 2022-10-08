# standart imports
from typing import List
from typing import Optional
from typing import Union

# third-party imports
from pydantic import BaseModel
from pydantic import Field

from typing_extensions import Literal


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


class ChoicesModel(BaseModel):
    ref: Optional[str]
    label: Optional[str]
    attachment: Optional[AttachmentModel]


class LabelModel(BaseModel):
    left: Optional[str]
    right: Optional[str]
    center: Optional[str]


class PropertiesModel(BaseModel):
    description: Optional[str]
    choices: Optional[List[ChoicesModel]]
    # TODO here should be FieldModel instead of dict
    fields: Optional[List[dict]]
    allow_multiple_selection: Optional[bool]
    randomize: Optional[bool]
    allow_other_choice: Optional[bool]
    vertical_alignment: Optional[bool]
    supersized: Optional[bool]
    show_labels: Optional[bool]
    alphabetical_order: Optional[bool]
    hide_marks: Optional[bool]
    button_text: Optional[str]
    steps: Union[None, float, int]
    shape: Optional[Literal[
        "cat",
        "circle",
        "cloud",
        "crown",
        "dog",
        "droplet",
        "flag",
        "heart",
        "lightbulb",
        "pencil",
        "skull",
        "star",
        "thunderbolt",
        "tick",
        "trophy",
        "up",
        "user",
    ]] = Field(default="star")
    labels: Optional[LabelModel]
    start_at_one: Optional[bool]
    structure: Optional[str]
    separator: Optional[Literal[
        "/",
        "-",
        ".",
    ]] = Field(default="/")
    currency: Optional[str]


class ValidationsModel(BaseModel):
    required: Optional[bool]
    max_length: Optional[int]
    min_value: Optional[int]
    max_value: Optional[int]
    min_selection: Optional[int]
    max_selection: Optional[int]


class LayoutModel(BaseModel):
    type_: Optional[str] = Field(alias="type")
    placement: Optional[Literal[
        "left",
        "right",
    ]]
    attachment: Optional[AttachmentModel]


class FieldModel(BaseModel):
    ref: Optional[str]
    title: str
    type_: Optional[Literal[
        "calendly",
        "date",
        "dropdown",
        "email",
        "file_upload",
        "group",
        "legal",
        "long_text",
        "matrix",
        "multiple_choice",
        "nps",
        "number",
        "opinion_scale",
        "payment",
        "phone_number",
        "picture_choice",
        "ranking",
        "rating",
        "short_text",
        "statement",
        "website",
        "website",
    ]]
    properties: Optional[PropertiesModel]
    validations: Optional[ValidationsModel]
    attachment: Optional[AttachmentModel]
    layout: Optional[LayoutModel]
