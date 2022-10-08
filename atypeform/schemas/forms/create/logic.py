# standart imports
from typing import Any
from typing import List
from typing import Optional

# third-party imports
from pydantic import BaseModel
from pydantic import Field

from typing_extensions import Literal


class ToModel(BaseModel):
    type_: Literal[
        "field",
        "thankyou",
        "outcome",
    ] = Field(alias="type")
    value: str


class TargetModel(BaseModel):
    type_: Literal["variable"] = Field(alias="type")
    value: Any


class ValueModel(BaseModel):
    type_: Literal[
        "constant",
        "variable",
        "evaluation",
    ] = Field(alias="type")
    value: Any


class DetailModel(BaseModel):
    to: Optional[ToModel]
    target: Optional[TargetModel]
    value: Optional[ValueModel]


class VarModel(BaseModel):
    type_: Literal[
        "field",
        "hidden",
        "variable",
        "constant",
        "choice",
    ] = Field(alias="type")
    value: Any


class ConditionModel(BaseModel):
    op: Literal[
        "begins_with",
        "ends_with",
        "contains",
        "not_contains",
        "lower_than",
        "lower_equal_than",
        "greater_than",
        "greater_equal_than",
        "is",
        "is_not",
        "equal",
        "not_equal",
        "always",
        "on",
        "not_on",
        "earlier_than",
        "earlier_than_or_on",
        "later_than",
        "later_than_or_on",
    ]
    vars_: List[VarModel] = Field(alias="vars")


class ActionModel(BaseModel):
    action: str
    details: DetailModel
    condition: ConditionModel


class LogicModel(BaseModel):
    type_: str = Field(alias="type")
    ref: Optional[str]
    actions: List[ActionModel]
