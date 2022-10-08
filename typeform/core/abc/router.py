# standart imports
from __future__ import annotations

import abc

from typing import Any


class AbstractRouter:
    def __init__(self) -> None:
        self.config = self.setup_config()
        self.routes = self.setup_routes()

    @abc.abstractmethod
    def setup_config(self) -> Any:
        raise NotImplementedError

    @abc.abstractmethod
    def setup_routes(self) -> Any:
        raise NotImplementedError

    @staticmethod
    def _format_url_kwargs(url_: str, **kwargs: Any) -> str:
        try:
            return url_.format(**kwargs)
        except KeyError:
            raise TypeError("Bad kwargs for url assembly")

    @abc.abstractmethod
    def build_url(self, api_method: str, **kwargs: Any) -> str:
        """Implementation of building url"""
        raise NotImplementedError
