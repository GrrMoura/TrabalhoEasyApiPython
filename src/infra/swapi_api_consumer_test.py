from .swapi_api_consumer import SwapiApiConsumer

def test_get_ship():
    swapi_api_consumer = SwapiApiConsumer()
    response = swapi_api_consumer.get_ship(page=1)
    print(response)