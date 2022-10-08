from __future__ import annotations

import abc
import copy

from types import TracebackType
from typing import Any
from typing import Dict
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import cast

# locale imports
from ..request_service import RequestService

_T = TypeVar("_T", bound="Wrapper")


class Wrapper(abc.ABC):
    __slots__ = ()

    @abc.abstractmethod
    def get_request_service(self) -> RequestService:
        raise NotImplementedError

    async def __aenter__(self):  # type: ignore
        await self.get_request_service().warmup()
        return self

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[TracebackType],
    ) -> None:
        pass
        await self.close()

    async def close(self) -> None:
        await self.get_request_service().shutdown()

    def _get(self, item: Any) -> Any:  # pragma: no cover
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return None

    def __deepcopy__(self, memo: Dict[Any, Any]) -> Wrapper:
        cls = self.__class__
        kw = {"__copy_signal__": True}
        result = cls.__new__(cls, **kw)  # type: ignore  # pragma: no cover
        memo[id(self)] = result
        instance_dictionary = {
            slot: self._get(slot)
            for slot in ["_request_service", "dispatcher"]
            if self._get(slot) is not None
        }
        for k, value in instance_dictionary.items():
            if k == "_request_service":
                value._holder = None
            elif k == "dispatcher":
                value._loop = None
            setattr(result, k, copy.deepcopy(value, memo))  # NOQA
        return cast(Wrapper, result)
