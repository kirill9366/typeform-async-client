# third-party imports
import pytest

# locale imports
from atypeform.schemas.webhooks import CreateRequestBodyModel
from atypeform.schemas.webhooks import CreateResponseBodyModel
from atypeform.schemas.webhooks import GetResponseBodyModel
from atypeform.settings import ApiRouter
from atypeform.webhooks import Webhooks


class TestWebhooks:

    _router = ApiRouter()
    _router.__head__ = "https://api.typeform.com"

    # webhook
    form_id = "lkZqriSX"
    tag = "child"
    form_id = "jJtGQNuC"

    async def test_get_list(self, client):
        webhooks = Webhooks(client, self._router)
        response = await webhooks.get(self.form_id)
        print(response)
        assert False
        assert isinstance(response, GetResponseBodyModel)

    # @pytest.mark.skip
    async def test_create(self, client):
        webhooks = Webhooks(client, self._router)
        response = await webhooks.create(
            "jJtGQNuC",
            "child",
            {
                "enabled": True,
                "url": "https://doc.prodvizhenie.org/webhook/child-deal",
            }
        )
        response = await webhooks.create(
            "lkZqriSX",
            "adult",
            {
                "enabled": True,
                "url": "https://doc.prodvizhenie.org/webhook/adult-deal",
            }
        )
        assert isinstance(response, CreateResponseBodyModel)

    @pytest.mark.skip
    async def test_delete(self, client):
        if not self.form_id:
            return

        webhooks = Webhooks(client, self._router)
        response = await webhooks.delete(self.form_id, self.tag)
        assert response.status == 204
