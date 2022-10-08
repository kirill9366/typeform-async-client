# local imports
from atypeform.core.request_service import RequestService
from atypeform.settings import ApiRouter


class TestRequestService:

    _service = RequestService()

    async def test_raw_request(self):
        response = await self._service.raw_request(
            "https://api.openweathermap.org/data/2.5/weather",
            "get",
            params={
                "appid": "ea9165cfe43f50d40672fb42dae01f3a",
                "lat": "33.44",
                "lon": "-94.04",
                "exclude": "hourly.daily",
            }
        )
        print(response)
        assert response.status == 200

    async def test_api_request(self):
        _router = ApiRouter()
        _router.__head__ = "https://api.openweathermap.org"
        response = await self._service.api_request(
            "get",
            "/data/2.5/weather",
            _router,
            params={
                "appid": "ea9165cfe43f50d40672fb42dae01f3a",
                "lat": "33.44",
                "lon": "-94.04",
                "exclude": "hourly.daily",
            }
        )
        print(response)
        assert response.status == 200
