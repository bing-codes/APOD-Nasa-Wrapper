#buidling a bespoke wrapper

import requests
import json
from PIL import Image
import urllib.request
import os


def generate_photo():
    
    while True:
        print("Welcome to the Astronomy Picture of the Day")
        print("You will need to enter a date after June 16, 1995")
        year = input("Year, format eg. 2020: ")
        month = input("Month, format eg. 12: ")
        day = input("Day, format eg. 13: ")
        date = f"{year}-{month}-{day}"

        #alternate way to format get request using parameters
        API_key = "" 
        endpoint = "https://api.nasa.gov/planetary/apod"
        params = {
            "api_key": API_key,
            "date": date
        }

        response = requests.get(endpoint, params=params)
        
        if response.status_code == 200 or response.status_code == 201:
            photo = response.json()
            image_url = photo.get("hdurl", photo["url"])

            title = photo["title"].replace(" ", "_")
            ext = image_url.split(".")[-1] 

            file_name = f"{title}.{ext}"
            urllib.request.urlretrieve(image_url, file_name)
            img = Image.open(file_name)

            return img

        else: 
            print("Please re-enter in the correct format!")

generate_photo()

