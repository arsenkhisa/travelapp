import mysql.connector

'''
origin = 'UFA'

destination = 'VVO'

when_date = '2023-05-18%'

back_date = '2023-05-20%'
'''


def get_data(departure_city, destination_city, departure_date, return_date):
    # Create the connection object
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="TheCloudKA2004",
        database="app"
    )

    # creating the cursor object
    cur = mydb.cursor()

    # Reading the Employee data
    query = "SELECT * FROM tickets WHERE origin = %s AND destination = %s" \
            "AND departure_date like %s AND return_date like %s"
    values = (departure_city, destination_city, departure_date, return_date)
    cur.execute(query, values)

    # fetching the rows from the cursor object
    result = cur.fetchall()

    for row in result:
        print("%d    %s    %s    %s    %s    %s    %s    %s    %s"
              % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    mydb.close()
