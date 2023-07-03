from typing import Dict, Optional, Any

import aiohttp

import simplejson

from pprint import pprint

# locale imports
from .abc.router import AbstractRouter


class RequestService:

    async def api_request(
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
    ) -> Dict[Any, Any]:
        url = router.build_url(api_method, **kwargs)
        return await self.raw_request(
            url,
            http_method,
            timeout=timeout,
            headers=headers,
            json=json,
            data=data,
            params=params,
        )

    async def raw_request(
        self,
        url: str,
        method: str,
        timeout: int = None,
        json: Optional[Any] = None,
        data: Optional[Any] = None,
        headers: Optional[Any] = None,
        params: Optional[Any] = None,
        **kwargs: Any
    ) -> Dict[Any, Any]:
        async with aiohttp.ClientSession() as session:
            return await session.request(
                method=method,
                url=url,
                data=data,
                headers=headers,
                json=json if isinstance(json, dict) else None,
                params=params,
                timeout=timeout,
                verify_ssl=False,
                **kwargs,
            )
