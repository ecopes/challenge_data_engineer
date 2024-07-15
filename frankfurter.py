import requests

FRANKFURTER_API_URL = "https://api.frankfurter.app"


def get_by_days(from_date: str, to_date: str) -> dict:
    """
    Gets data from Frankfurter
    :param from_date: format -> 'YYYY-MM-DD'
    :param to_date: format -> 'YYYY-MM-DD'
    :return:
    example:
        {'2024-02-13': {'AUD': 1.6526,
                        'BGN': 1.9558,
                        'BRL': 5.3465,
                        'CAD': 1.4511,
                        'CHF': 0.9481,
                        'CNY': 7.7641,
                        'CZK': 25.285,
                        'DKK': 7.4548,
                        'GBP': 0.85098,
                        'HKD': 8.4372,
                        'HUF': 387.0,
                        'IDR': 16850,
                        'ILS': 3.9322,
                        'INR': 89.58,
                        'ISK': 148.7,
                        'JPY': 161.17,
                        'KRW': 1434.64,
                        'MXN': 18.4272,
                        'MYR': 5.1439,
                        'NOK': 11.302,
                        'NZD': 1.7636,
                        'PHP': 60.398,
                        'PLN': 4.3198,
                        'RON': 4.9759,
                        'SEK': 11.251,
                        'SGD': 1.451,
                        'THB': 38.52,
                        'TRY': 33.16,
                        'USD': 1.0793,
                        'ZAR': 20.318},
         '2024-02-14': {'AUD': 1.6526...},
        }

    """
    response = requests.get(f"{FRANKFURTER_API_URL}/{from_date}..{to_date}", )
    response.raise_for_status()
    data = response.json()
    return data.get("rates")
