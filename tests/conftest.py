# third-party imports
import pytest_asyncio

from decouple import config

# locale imports
from atypeform.client import Client
from atypeform.core.request_service import RequestService


@pytest_asyncio.fixture(name="client")
async def client_fixture():
    token = config("TYPEFORM_TOKEN")
    return Client(token, RequestService())
