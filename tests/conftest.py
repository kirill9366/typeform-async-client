# third-party imports
import pytest_asyncio

from decouple import config

# locale imports
from typeform.client import Client
from typeform.core.request_service import RequestService


@pytest_asyncio.fixture(name="client")
async def client_fixture():
    token = config("TYPEFORM_TOKEN")
    return Client(token, RequestService())
