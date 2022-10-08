# locale imports
from .core.request_service import RequestService
from .settings import ApiRouter
from .forms import Forms
# from .responses import Responses
from .client import Client

__all__ = ["AsyncTypeform"]


class AsyncTypeform:
    """Typeform API client"""

    def __init__(self, token: str, headers: dict = {}):
        """Constructor for Typeform API client"""

        service = RequestService()
        client = Client(token, service)
        router = ApiRouter()
        self.__forms = Forms(client, router)
        # self.__responses = Responses(client)

    @property
    def forms(self) -> Forms:
        return self.__forms

    # @property
    # def responses(self) -> Responses:
        # return self.__responses
