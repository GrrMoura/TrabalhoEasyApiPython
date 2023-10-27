from typing import Dict,Tuple, Type
import requests
from requests import Request
from collections import namedtuple
from src.errors import HttpRequestError


class SwapiApiConsumer():
    """docstring for ClassName."""
    def __init__(self) -> None:
        self.get_ship_response = namedtuple("Get_Ship", "status_code request response")
 
    def get_ship(self, page:int) -> tuple[int, Type[Request],Dict]:
        """preparando a requisição"""
        req = requests.Request(
            method="GET",
            url="https://swapi.dev/api/starships",
            params={'page':page}            
        )
         
        req_preparada = req.prepare()
        
        response=self.__send_http_request(req_preparada) 
        status_code = response.status_code
        
        if (status_code>=200 and status_code <=299):
            return self.get_ship_response(status_code= status_code, request= req, response=response.json())
        
        else:
            raise HttpRequestError(
                message = response.json()['detail'], status_code=status_code            )

        
    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> any:
        http_session = requests.session()
        response = http_session.send(req_prepared)
        return response

    