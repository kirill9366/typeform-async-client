# standart imports
import json
import os

# locale imports
from atypeform.schemas.forms.list import ResponseBodyModel


class TestResponseBodyModel:

    def test_parse_obj(self):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(f"{path}/data/list.json", "r") as file:
            data = json.load(file)
            ResponseBodyModel.parse_obj(data)
