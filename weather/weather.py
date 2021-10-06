import requests


def show_weather(location: str, language: str, unit: str) -> None:
    """Print weather into terminal.

    Args:
        location: city or aiport ICAO
        language: `ru` or `en`
        unit: `u` for USCS system, `m` for SI system.

    """
    payload = {
        'n': '',
        'T': '',
        'q': '',
        'lang': language,
        unit: '',
    }

    url = f'http://wttr.in/{location}'
    resp = requests.get(url, params=payload)
    resp.raise_for_status()
    print(resp.text)


def main() -> None:
    url_params = [
        ('Лондон', 'en', 'u'),
        ('SVO', 'en', 'u'),
        ('Череповец', 'ru', 'm')
    ]
    for args in url_params:
        show_weather(*args)


if __name__ == '__main__':
    main()
