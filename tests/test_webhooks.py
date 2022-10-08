# locale imports
from typeform.schemas.webhooks import CreateRequestBodyModel
from typeform.schemas.webhooks import CreateResponseBodyModel
from typeform.schemas.webhooks import GetResponseBodyModel
from typeform.settings import ApiRouter
from typeform.webhooks import Webhooks


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
