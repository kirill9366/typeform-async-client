# standart imports
from typing import Optional

# third-party imports
from pydantic import BaseModel
from pydantic import Field

from typing_extensions import Literal


class ImageModel(BaseModel):
    href: Optional[str]


class MetaModel(BaseModel):
    title: Optional[str]
    allow_indexing: Optional[bool]
    description: Optional[str]
    image: Optional[ImageModel]


class SettingsModel(BaseModel):
    language: Optional[Literal[
        "en",
        "es",
        "ca",
        "fr",
        "de",
        "ru",
        "it",
        "da",
        "pt",
        "ch",
        "zh",
        "nl",
        "no",
        "uk",
        "ja",
        "ko",
        "hr",
        "fi",
        "sv",
        "pl",
        "el",
        "hu",
        "tr",
        "cs",
        "et",
        "di",
    ]]
    is_public: Optional[bool]
    progress_bar: Optional[Literal[
        "percentage",
        "proportion",
    ]] = Field(default="proportion")
    show_progress_bar: Optional[bool]
    show_typeform_branding: Optional[bool]
    show_time_to_complete: Optional[bool]
    show_number_of_submissions: Optional[bool]
    show_cookie_consent: Optional[bool]
    show_question_number: Optional[bool]
    hide_navigation: Optional[bool]
    meta: Optional[MetaModel]
    redirect_after_submit_url: Optional[str]
    google_analytics: Optional[str]
    facebook_pixel: Optional[str]
    google_tag_manager: Optional[str]
