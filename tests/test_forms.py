# standart imports
import json
import os

# locale imports
from typeform.forms import Forms
from typeform.schemas.forms import CreateRequestBodyModel
from typeform.schemas.forms import ListResponseBodyModel
from typeform.settings import ApiRouter


class TestForms:

    _router = ApiRouter()
    _router.__head__ = "https://api.typeform.com"

    async def test_get_list(self, client):

        forms = Forms(client, self._router)
        response = await forms.get_list()
        assert isinstance(response, ListResponseBodyModel)
