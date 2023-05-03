import requests
import mysql.connector

city_url = "https://api.travelpayouts.com/data/en/cities.json"
city_response = requests.get(city_url)
city_data = city_response.json()

iata_codes = []

for city in city_data:
    if city['country_code'] == 'RU':
        iata_codes.append(city['code'])
iata_codes.sort()

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="TheCloudKA2004",
    database="app"
)

mycursor = mydb.cursor()

url = "https://api.travelpayouts.com/v2/prices/latest"

for origin_code in range(len(iata_codes)):
    flag = requests.get(url,
                        params={'origin': iata_codes[origin_code],
                                'destination': 'MOW',
                                'token': '9570cd803e10001a719af1e9aba6835a'})
    check = flag.json()
    if (check['success'] is True) and (len(check['data']) != 0):
        for destination_code in range(len(iata_codes)):
            response = requests.get(url,
                                    params={'currency': 'rub',
                                            'origin': iata_codes[origin_code],
                                            'destination': iata_codes[destination_code],
                                            'token': '9570cd803e10001a719af1e9aba6835a'})
            data = response.json()
            print(iata_codes[origin_code], "    ", iata_codes[destination_code])

            if (data['success'] is True) and (len(data['data']) != 0):
                print(data['data'])
                for i in range(len(data['data'])):
                    sql = "INSERT INTO tickets (origin, destination, departure_date, return_date, price)" \
                          " VALUES (%s, %s, %s, %s, %s)"
                    val = (data['data'][i]['origin'], data['data'][i]['destination'],
                           data['data'][i]['depart_date'], data['data'][i]['return_date'],
                           data['data'][i]['value'])
                    mycursor.execute(sql, val)
                    mydb.commit()

    else:
        origin_code += 1

mydb.close()
