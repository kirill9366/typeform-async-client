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
    form_id = "jJtGQNuC"
    tag = "phoenix"

    async def test_get_list(self, client):
        webhooks = Webhooks(client, self._router)
        response = await webhooks.get("jJtGQNuC")
        print(response)
        assert isinstance(response, GetResponseBodyModel)

    async def test_create(self, client):
        webhooks = Webhooks(client, self._router)
        response = await webhooks.create(
            self.form_id,
            self.tag,
            {
                "enabled": True,
                "url": "https://example.com",
            }
        )
        assert isinstance(response, CreateResponseBodyModel)

    async def test_delete(self, client):
        if not self.form_id:
            return

        webhooks = Webhooks(client, self._router)
        response = await webhooks.delete(self.form_id, self.tag)
        assert response.status == 204
