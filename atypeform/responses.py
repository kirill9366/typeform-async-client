# standart imports
import typing

# locale imports
from .client import Client
from .core.abc.router import AbstractRouter
from .schemas.responses import ListResponseBodyModel
from .settings import ApiMethods

from datetime import datetime


class Responses:
    """Typeform Responses API client"""

    def __init__(self, client: Client, router: AbstractRouter):
        """Constructor for Typeform Responses class"""
        self._client = client
        self._router = router

    async def get_list(
        self,
        form_id: str,
        page_size: int = 1,
        after: str = None,
    ) -> typing.Union[
        dict,
        ListResponseBodyModel,
    ]:
        """Get List of Responses.

        Parameters
        ----------
        form_id : str
            ID of Form.
        page_size : int default: 25
            Count of form Responses.

        Returns
        -------
        ListResponseBodyModel
            Everything is correct.
        dict
            Typeform returned an error.

        """
        response = await self._client.request(
            "get",
            ApiMethods.LIST_RESPONSES.format(form_id),
            self._router,
            params={
                "page_size": page_size,
                "after": after,
            },
            timeout=3,
        )
        if response.status == 200:
            return ListResponseBodyModel.parse_obj(
                await response.json()
            )
        return response
