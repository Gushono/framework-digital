import os
from abc import ABC, abstractmethod
from typing import List

import requests
from requests import Response

from server import Unauthorized, NotFound, logger


class Requester(ABC):
    def __init__(self, headers=None):

        if not headers:
            self.headers = {}

    @abstractmethod
    def get_method(self, path: str, params=None) -> List[dict] or dict:
        """
        Get Request
        """

        pass

    @abstractmethod
    def validate_response(self, response: Response) -> bool:
        """
        Validate if a response of a get_request is valid
        """
        pass


class RequestToJsonPlaceHolder(Requester):
    __URL = os.getenv("URL_JSON_PLACE_HOLDER") or 'https://jsonplaceholder.typicode.com'

    def get_method(self, path: str, params=None) -> List[dict] or dict:
        logger.info(f"Get in {self.__URL + path}...\n")
        response: Response = requests.get(self.__URL + path, params=params)

        response_validated = self.validate_response(response)

        return response_validated

    def validate_response(self, response: Response) -> dict:
        """
        It consideres only status_code 200 and 204 valid.

        :param response: Response of the request to get the CSV file
        """

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            raise Unauthorized(message=f"Request to {self.__URL} is unauthorized")
        elif response.status_code == 404:
            raise NotFound(message="Entity not found")
