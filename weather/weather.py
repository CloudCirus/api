import requests


"""
location - city or airport ICAO using ru/en, example: 'Moscow', 'SVO'
language - 'ru'/'en'
unit - 'u' = USCS system for USA  / 'm' = SI system for Europe and others country
full doc: http://wttr.in/:help
"""


def show_weather(location: str, language: str, unit: str):
    payload = {'lang': f'{language}'}
    url = f'http://wttr.in/{location}?nTq{unit}'
    resp = requests.get(url, params=payload)
    resp.raise_for_status()
    print(resp.text)


show_weather('Лондон', 'en', 'u')
show_weather('SVO', 'en', 'u')
show_weather('Череповец', 'ru', 'm')
