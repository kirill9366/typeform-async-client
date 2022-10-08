# standart imports
from typing import Any
from typing import List
from typing import Optional

# third-party imports
from pydantic import BaseModel
from pydantic import Field

from typing_extensions import Literal

# locale imports
from .cui_settings import CuiSettingsModel
from .fields import FieldModel
from .logic import LogicModel
from .settings import SettingsModel
from .thankyou_screen import ThankYouScreenModel
from .variables import VariablesModel
from .welcome_screen import WelcomeScreenModel
from .workspace import WorkSpaceModel


class RequestBodyModel(BaseModel):

    cui_settings: Optional[CuiSettingsModel]
    fields: Optional[List[FieldModel]]
    hidden: Optional[List[str]]
    logic: Optional[List[LogicModel]]
    settings: Optional[SettingsModel]
    thankyou_screens: Optional[List[ThankYouScreenModel]]
    theme: Any
    title: Optional[str]
    type_: Optional[Literal[
        "quiz",
        "classification",
        "score",
        "branching",
        "classification_branching",
        "score_branching",
        "form",
    ]] = Field(alias="type")
    variables: Optional[VariablesModel]
    welcome_screens: Optional[List[WelcomeScreenModel]]
    workspace: Optional[WorkSpaceModel]
