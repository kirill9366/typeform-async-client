from typing import Any

# locale imports
from .core.abc.router import AbstractRouter

from .utils.mypy_hacks import lru_cache


class ApiMethods:

    # CRUD
    ADD_ACCOUNT: str = '/api/addAccount'
    UPDATE_ACCOUNT: str = '/api/updateAccount'
    DELETE_ACCOUNT: str = '/api/deleteAccount'

    # start and stop account
    SET_STATE: str = '/api/setState'
    FORCE_STOP: str = '/api/forceStop'
    CLEAR: str = '/api/clear'

    # auth
    TWO_FACTOR_AUTH: str = '/api/twoFactorAuth'
    START_CHALLENGE: str = '/api/startChallenge'
    SOLVE_CHALLENGE: str = '/api/solveChallenge'

    # chat
    GET_CHATS: str = '/api/getChats'
    GET_CHAT_MESSAGES: str = '/api/getChatMessages'
    SEND_MESSAGE: str = '/api/sendMessage'

    # info
    GET_INFO: str = '/api/getInfo'
    GET_USER_INFO: str = '/api/getUserInfo'

    # config
    GET_CONFIG_LIST: str = '/api/getConfigList'
    GET_CONFIG: str = '/api/getConfig'
    SET_CONFIG: str = '/api/setConfig'
    GENERATE_NEW_DEVICE: str = '/api/generateNewDevice'

    # comments
    SEND_COMMENT: str = '/api/sendComment'
    GET_MEDIA_COMMENTS: str = '/api/getMediaComments'


class ApiConfig:
    pass


class ApiRouter(AbstractRouter):

    __head__ = "https://api.openweathermap.org"

    def setup_routes(self) -> ApiMethods:
        return ApiMethods()

    def setup_config(self) -> ApiConfig:
        return ApiConfig()

    @lru_cache(typed=True)
    def build_url(self, api_method: str, **kwargs: Any) -> str:
        pre_build_url = self.__head__ + api_method
        return super()._format_url_kwargs(pre_build_url, **kwargs)
