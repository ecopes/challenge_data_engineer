from enum import Enum

import pandas as pd
from pandasql import sqldf

from fake_store import get_all_products_by_category
from frankfurter import get_by_days


class Category(Enum):
    """
    I'm using an Enum, buy you can use the plain string as well
    """
    ELECTRONICS = "electronics"
    JEWELERY = "jewelery"
    MENS_CLOTHING = "men's clothing"
    WOMENS_CLOTHING = "women's clothing"


def add_attributes_to_product(product: dict, exchange_value: float, exchange_date: str):
    """
    here I'm adding the attributes I need for complete the challenge
    """
    usd_price = float(product["price"])
    rating = product["rating"]
    del product["rating"]
    product['usd_price'] = usd_price
    product['eur_price'] = usd_price / exchange_value
    product['exchange_date'] = exchange_date
    product['rating_value'] = rating['rate']
    product['rating_count'] = rating['count']
    return product


# here I'm getting all the exchange data, in this case, only for 2 days, buy can be from/to how many days you want
exchange_data = get_by_days(from_date="2024-02-12", to_date="2024-02-13")
all_products = []
for exchange_date in exchange_data:
    """
    I'm getting all the products filtered by category with the method
    get_all_products_by_category(Category.WOMENS_CLOTHING.value)
    then running 1 by 1 to add the information I need with the function add_attributes_to_product and add those
    to the list all_products
    """
    products = [add_attributes_to_product(product=p, exchange_value=float(exchange_data[exchange_date]['USD']),
                                          exchange_date=exchange_date) for p in
                get_all_products_by_category(Category.WOMENS_CLOTHING.value)]
    all_products.extend(products)

# I create a dataFrame with the list of products
df = pd.DataFrame(all_products)

"""
I'm defining the query that I'm going to run to the table, but in this case I'm using sqldf to run the query against
the dataframe instead, this query can be performed against a database as well
the only "weird" thing here is the sentence
ROW_NUMBER() OVER (PARTITION BY exchange_date ORDER BY rating_value DESC) AS ranking
that is counting the rows by exchange_date, ordering by rating_value
"""
query = """
    SELECT *
    FROM (
        SELECT *,
               ROW_NUMBER() OVER (PARTITION BY exchange_date ORDER BY rating_value DESC) AS ranking
        FROM df
    ) AS ranked_data
    WHERE ranking <= 5;
"""

# Execute the SQL query
result_df = sqldf(query, globals())

print("Result DataFrame:")
print(result_df)

"""
QUESTIONS:

Q: Using typical sales data as an example, how would you ensure that a data pipeline is kept
up to date with accurate data? 

A: I would add a check with a common json and the data we are receiving, on the function add_attributes_to_product
 or maybe run one check before that function (like a middleware) if the job runs and the data we are receiving 
 is different, I would send a message to slack (or another alert type) so the data is going to be "not updated" 
 until someone fix that, but is not going to be wrong
 
Q: What tools or processes might you use so that sales data is
updated daily?
A: A cron job that runs every certain period of time that updates the data, with AWS lambda functions

Q: Our sales and product data are constantly changing—returns can affect previous sales, and
pricing changes can affect product data tables, etc. How would you go about building a data
pipeline that is able to add new data while also changing or updating existing data that has
changed at the source system?
A: For the new data, the way I did it is ok, is going to add that new attributes without problem. For modifying the
old data, you have to do even a SQL query update or a job that update them all at once
"""