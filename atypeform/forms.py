# standart imports
import typing

# locale imports
from .client import Client
from .core.abc.router import AbstractRouter
from .schemas.forms import CreateRequestBodyModel
from .schemas.forms import ListResponseBodyModel
from .settings import ApiMethods


class Forms:
    """Typeform Forms API client"""

    def __init__(self, client: Client, router: AbstractRouter):
        """Constructor for Typeform Forms class"""
        self._client = client
        self._router = router
        # self.__messages = FormMessages(service)

    async def get_list(self) -> typing.Union[
        dict,
        ListResponseBodyModel,
    ]:
        """"""
        response = await self._client.request(
            "get",
            ApiMethods.LIST_FORMS,
            self._router,
        )
        if response.status == 200:
            return ListResponseBodyModel.parse_obj(
                await response.json()
            )
        return response

    async def delete(self, form_id: str) -> str:
        """Deletes a form with the specified form_id.

        Parameters
        ----------
        form_id : str
            Form ID

        """
        return await self._client.request(
            "delete",
            ApiMethods.DELETE_FORM.format(form_id),
            self._router,
        )
