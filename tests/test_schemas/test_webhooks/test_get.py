# standart imports
import json
import os

# third-party imports
from atypeform.schemas.webhooks import GetResponseBodyModel


class TestResponseBodyModel:

    def test_parse_obj(self):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(f"{path}/data/get_response.json", "r") as file:
            data = json.load(file)
            model = GetResponseBodyModel.parse_obj(data)
            item = model.items[0]

        assert item.created_at == "2016-11-21T12:23:28Z"
        assert item.enabled
        assert item.form_id == "abc123"
        assert item.id_ == "yRtagDm8AT"
        assert item.tag == "phoenix"
        assert item.updated_at == "2016-11-21T12:23:28Z"
        assert item.url == "https://test.com"
        assert item.verify_ssl
