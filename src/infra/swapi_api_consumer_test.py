from .swapi_api_consumer import SwapiApiConsumer
from  src.errors import HttpRequestError

def test_get_ship(requests_mock):
    requests_mock.get('https://swapi.dev/api/starships', status_code=200, json={'some':"thing", "results": [{}]})
    swapi_api_consumer = SwapiApiConsumer()
   
    page =1
    
    get_ship_response= swapi_api_consumer.get_ship(page=page)
    assert get_ship_response.request.method=="GET"
    assert get_ship_response.request.url=="https://swapi.dev/api/starships"
    assert get_ship_response.request.params=={"page":page}
   
    assert get_ship_response.status_code==200
    assert isinstance(get_ship_response.response['results'],list)
    


    
def teste_get_ship_http_error(requests_mock):
    swapi_api_consumer = SwapiApiConsumer()
    page = 1    
    requests_mock.get('https://swapi.dev/api/starships', status_code=404, json={'detail': "something"})
    
    try:
        swapi_api_consumer.get_ship(page=page)
        assert True is False
    except HttpRequestError as error:
         assert error.message is not None
         assert error.status_code is not None
         print(error.message)
         print(error.status_code)
      