# standart imports
import json
import os

# locale imports
from atypeform.schemas.forms.create import RequestBodyModel


class TestRequestBodyModel:

    def test_parse_obj(self):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(f"{path}/data/create.json", "r") as file:
            data = json.load(file)
            RequestBodyModel.parse_obj(data)
