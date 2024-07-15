import requests

FAKE_STORE_API_URL = "https://fakestoreapi.com"


def get_all_products_by_category(category: str) -> list:
    """
    Gets all products from a category
       :return: A dictionary
       :param category: The category of the products, examples: [
            "electronics",
            "jewelery",
            "men's clothing",
            "women's clothing"
            ]
        :return: A list of dicts example:
        [{'category': "women's clothing",
         'description': 'Note:T....,
         'id': 15,
         'image': 'https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_.jpg',
         'price': 56.99,
         'rating': {'count': 235, 'rate': 2.6},
         'title': "BIYLACLESEN Women's 3-in-1 Snowboard Jacket Winter Coats"}, ]
    """
    response = requests.get(f"{FAKE_STORE_API_URL}/products/category/{category}")
    if response.status_code == 200:
        return response.json()
