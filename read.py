"""
Made by - 
Rohan Shingre - MSM19B012

ThingSpeak Fields:
1) Field 1: Temperature
2) Field 2: Humidity
3) Field 3: Light
4) Field 4: Pressure
Read API Endpoint: https://api.thingspeak.com/channels/1312819/feeds.json?api_key=C2BX4LOOP9PEULZG&results=5
"""
import requests, sqlite3

response = requests.get(
    "https://api.thingspeak.com/channels/1312819/feeds.json?api_key=C2BX4LOOP9PEULZG&results=5"
)

if(response.ok):
    response_in_json = response.json()
else:
    exit(1) #Exiting if we get Invalid Response

data = response_in_json.get("feeds")

connection = connection = sqlite3.connect("response.db")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE Response (Id INTEGER,Temperature INTEGER, Humidity INTEGER, Light INTEGER, Pressue INTEGER)"
) 

for i in data:
    id_ = i['entry_id']
    temperature = int(i['field1'])
    humidity = int(i['field2'])
    light = int(i['field3'])
    pressure = int(i['field4'])

    cursor.execute(f"INSERT INTO Response VALUES ({id_}, {temperature}, {humidity}, {light}, {pressure})")


connection.commit() 

print("Sucessfully Written Response from thingSpeak in database.")