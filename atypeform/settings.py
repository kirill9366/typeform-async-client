from typing import Any

# locale imports
from .core.abc.router import AbstractRouter

from .utils.mypy_hacks import lru_cache


class ApiMethods:

    # forms
    CREATE_FORM: str = "/forms"
    DELETE_FORM: str = "/forms/{}"
    LIST_FORMS: str = "/forms"

    # webhooks
    GET_WEBHOOK: str = "/forms/{}/webhooks"
    CREATE_WEBHOOK: str = "/forms/{}/webhooks/{}"
    DELETE_WEBHOOK: str = "/forms/{}/webhooks/{}"

    # responses
    LIST_RESPONSES: str = "/forms/{}/responses"


class ApiConfig:
    pass


class ApiRouter(AbstractRouter):

    __head__ = "https://api.typeform.com"

    def setup_routes(self) -> ApiMethods:
        return ApiMethods()

    def setup_config(self) -> ApiConfig:
        return ApiConfig()

    @lru_cache(typed=True)
    def build_url(self, api_method: str, **kwargs: Any) -> str:
        pre_build_url = self.__head__ + api_method
        return super()._format_url_kwargs(pre_build_url, **kwargs)
