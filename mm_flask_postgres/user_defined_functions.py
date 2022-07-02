from urllib.request import urlopen
import json
import requests

#Function for getting Json data from CDN
def ud_getCdnJson(url):   
    # store the response of URL
    response = urlopen(url)
        
    # storing the JSON response
    # from url in data
    data_json = json.loads(response.read())
        
    return data_json


######################################

#Function for getting Json data from CDN
def ud_requestCdnJson(url): 
    # store the response of URL
    response = requests.get(url)

    # storing the JSON response
    # from url in data
    data_json = response.json()
    print(data_json)
    return data_json

