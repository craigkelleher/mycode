#!/usr/bin/python3
import datetime
import requests
import reverse_geocoder as rg

## Define URL
URL = 'http://api.open-notify.org/iss-now.json'

def main():
    ## Call the webservice
    response = requests.get(URL).json()

    longitude = response["iss_position"]["longitude"]
    latitude = response["iss_position"]["latitude"]

    city = rg.search((latitude, longitude))[0]["name"]
    country = rg.search((latitude, longitude))[0]["cc"]
    
    timestamp = response["timestamp"]
    # epoc time to datetime python in UTC 
    timestamp = datetime.datetime.fromtimestamp(timestamp).strftime("%a, %d %b %Y %H:%M:%S UTC")

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Timestamp:\t\t {timestamp}
    Longitude:\t\t {longitude}
    Latitude:\t\t {latitude}
    City/Country:\t {city}, {country}
    """)

if __name__ == "__main__":
    main()
