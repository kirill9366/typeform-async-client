# standart imports
import typing

# locale imports
from .client import Client
from .core.abc.router import AbstractRouter
from .schemas.webhooks import CreateRequestBodyModel
from .schemas.webhooks import CreateResponseBodyModel
from .schemas.webhooks import GetResponseBodyModel
from .settings import ApiMethods


class Webhooks:
    """Typeform Forms API client"""

    def __init__(self, client: Client, router: AbstractRouter):
        """Constructor for Typeform Forms class"""
        self._client = client
        self._router = router
        # self.__messages = FormMessages(service)

    async def get(self, form_id: str) -> dict:
        """Get Webhooks

        Parameters
        ----------
        form_id : str
            Form ID from TypeForm

        """
        response = await self._client.request(
            "get",
            ApiMethods.GET_WEBHOOK.format(form_id),
            self._router,
        )
        if response.status == 200:
            return GetResponseBodyModel.parse_obj(
                await response.json()
            )
        return response

    async def create(
        self,
        form_id: str,
        tag: str,
        data: typing.Union[CreateRequestBodyModel, dict],
    ):
        """Create webhook

        Parameters
        ----------
        form_id : str
            Form ID From TypeForm
        tag : str
            Webhook tag
        data : CreateRequestBodyModel
            Additional data for webhook

        """
        if isinstance(data, CreateResponseBodyModel):
            data = data.dict()

        response = await self._client.request(
            "put",
            ApiMethods.CREATE_WEBHOOK.format(form_id, tag),
            self._router,
            json=data,
        )
        if response.status == 200:
            return CreateResponseBodyModel.parse_obj(
                await response.json()
            )
        return response

    async def delete(
        self,
        form_id: str,
        tag: str,
    ):
        """Delete webhook

        Parameters
        ----------
        form_id : str
            Form ID From TypeForm
        tag : str
            Webhook tag

        """
        return await self._client.request(
            "delete",
            ApiMethods.DELETE_WEBHOOK.format(form_id, tag),
            self._router,
        )
