import requests
from pprint import pprint

API_KEY = '2575|3jZRe2pHmarqONP4dCiCc3Ihrav9Rk1WghmwKyak'

def get_country(name):

    URL = f"https://restfulcountries.com/api/v1/countries/{name}"

    req_headers = {
        'Accept':'application/json',
        'Authorization':f'Bearer {API_KEY}'
    }


    try:
        response = requests.get(url=URL, headers=req_headers)

        country = response.json()
        name = country['data']['name']
        president = country['data']['current_president']['name']
        photo = country['data']['current_president']['href']['picture']
        description = country['data']['description']
        covid = country['data']['covid19']['total_case']

    # return(f'Nazwa kraju to {name} a jego prezydent ma na imię {president}.\nOto krótki opis kraju'
    #       f' wraz z linkiem do zdjęcia prezydenta {photo}.\nPrzypadków covid było {covid}')

        print(f'Nazwa kraju to {name} a jego prezydent ma na imię {president}.\nOto krótki opis kraju'
              f' wraz z linkiem do zdjęcia prezydenta {photo}.\nPrzypadków covid było {covid}')

    except KeyError as ke:
        print('Nie znaleziono klucza', ke)
        print(ke)
    except Exception as er:
        print('Wystąpił błąd', er)
        print(er)

get_country('Poland')

#print(get_country())