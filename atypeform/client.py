# standart imports
from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

# third-party imports

# locale imports
from .core.abc.router import AbstractRouter
from .core.request_service import RequestService


class Client(object):
    """TypeForm API HTTP client"""

    def __init__(self, token: str, service: RequestService):
        """Constructor for TypeForm API client"""
        self._headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"bearer {token}"
        }
        self._service = service

    async def request(
        self,
        http_method: str,
        api_method: str,
        router: AbstractRouter,
        timeout: int = None,
        json: Optional[Any] = None,
        data: Optional[Dict[Any, Any]] = None,
        headers: Optional[Dict[Any, Any]] = None,
        params: Optional[Dict[Any, Any]] = None,
        **kwargs: Any
    ) -> Union[str, dict]:
        if headers:
            self._headers += headers
        return await self._service.api_request(
            http_method,
            api_method,
            router,
            timeout=timeout,
            headers=self._headers,
            json=json,
            data=data,
            params=params,
            **kwargs
        )
