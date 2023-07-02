# standart imports
import json
import os

# locale imports
from atypeform.responses import Responses
from atypeform.schemas.responses import ListResponseBodyModel
from atypeform.settings import ApiRouter


class TestResponses:

    _router = ApiRouter()
    _router.__head__ = "https://api.typeform.com"

    async def test_get_list(self, client):

        responses = Responses(client, self._router)
        response = await responses.get_list("jJtGQNuC", page_size=1)
        print(response)
        assert False
        assert isinstance(response, ListResponseBodyModel)
