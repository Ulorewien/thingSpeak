"""
Made by - 
Rohan Shingre - MSM19B012

ThingSpeak Fields:
1) Field 1: Temperature
2) Field 2: Humidity
3) Field 3: Light
4) Field 4: Pressure
Write API Endpoint: https://api.thingspeak.com/update?api_key=XYTKALOJOT960JX5&field1=0
"""

import requests, random, time

try:
    while True:
        temperature = random.randint(1,45)
        humidity = random.randint(10,30)
        light = random.randint(1,10)
        pressure = random.randint(1,80)

        response = requests.get(
            "https://api.thingspeak.com/update?api_key=XYTKALOJOT960JX5",
            params={'field1':temperature,'field2':humidity,'field3':light,'field4':pressure}
        )

        print(f"Status {response.status_code}")
        time.sleep(0.5)
except:
    print("\nExiting due to Error...")
