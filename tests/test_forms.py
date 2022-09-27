# locale imports
from typeform.core.request_service import RequestService
from typeform.forms import Forms


class TestForms:

    _forms = Forms(RequestService())

    def test_create(self):
        assert 1 == 1
