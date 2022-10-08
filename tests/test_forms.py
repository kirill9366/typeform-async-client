# standart imports
import json
import os

# locale imports
from atypeform.forms import Forms
from atypeform.schemas.forms import CreateRequestBodyModel
from atypeform.schemas.forms import ListResponseBodyModel
from atypeform.settings import ApiRouter


class TestForms:

    _router = ApiRouter()
    _router.__head__ = "https://api.typeform.com"

    async def test_get_list(self, client):

        forms = Forms(client, self._router)
        response = await forms.get_list()
        assert isinstance(response, ListResponseBodyModel)
