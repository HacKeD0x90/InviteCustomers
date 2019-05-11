## Dependencies

1. Python 2.7 (exist by default)
2. sudo apt-get install python-pip
3. sudo pip install geopy

## How to run
python GetNearestCustomer.py customers.json > output.txt

## Screenshot
![Intercom](http://sakr.gq/images/Intercom.png "Script in action")

## Description
We have some customer records in a text file (customers.txt) -- one customer per line, JSON lines formatted. We want to invite any customer within 100km of our Dublin office for some food and drinks on us. Write a program that will read the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID (ascending).

* You must use the first formula from this Wikipedia article to calculate distance. Don't forget, you'll need to convert degrees to radians.
* The GPS coordinates for our Dublin office are 53.339428, -6.257664.

# How to Solve.
First of all the geopy library implements the Great-circle distance formula withing one of it's functions called greate_circle, if we take a look on the source code we will find it's pretty much the same as the first formula.
![Intercom](http://sakr.gq/images/great.png "Formula Used")

1. Parse the json file to customer class.
2. Calculate the distance between each customer and Intercom.
3. If the distance is less than or equal 100KM , insert it in a list.
4. sort the list acoording to user_id parameter
