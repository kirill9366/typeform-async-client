# standart imports
import json
import os

# third-party imports
from atypeform.schemas.webhooks import CreateRequestBodyModel
from atypeform.schemas.webhooks import CreateResponseBodyModel


class TestRequestBodyModel:

    def test_parse_obj(self):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(f"{path}/data/create_request.json", "r") as file:
            data = json.load(file)
            model = CreateRequestBodyModel.parse_obj(data)

        assert model.enabled is True
        assert model.url == "https://test.com"


class TestResponseBodyModel:

    def test_parse_obj(self):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(f"{path}/data/create_response.json", "r") as file:
            data = json.load(file)
            model = CreateResponseBodyModel.parse_obj(data)

        assert model.created_at == "2016-11-21T12:23:28Z"
        assert model.enabled
        assert model.form_id == "abc123"
        assert model.id_ == "yRtagDm8AT"
        assert model.tag == "phoenix"
        assert model.updated_at == "2016-11-21T12:23:28Z"
        assert model.url == "https://test.com"
        assert model.verify_ssl
