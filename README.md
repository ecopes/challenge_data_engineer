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