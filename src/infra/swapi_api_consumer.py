import requests


class SwapiApiConsumer(object):
    """docstring for ClassName."""
    
    @classmethod
    def get_ship(self, page:int):
     params= {'page':page}
     response = requests.get('https://swapi.dev/api/starships',params=params)
     return response.json()
   

    