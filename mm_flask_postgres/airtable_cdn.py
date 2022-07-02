
from urllib.request import urlopen
import json
import requests

#Function for getting Json data from CDN
def my_getCdnJson(url):   
    # store the response of URL
    response = urlopen(url)
        
    # storing the JSON response
    # from url in data
    # data_json = json.loads(response.read())
    data_json = json.load(response)
        
    return data_json


################################################################

def my_getStaffCdnJson():
    staffCdnUrl = 'https://cdn.baseboosters.com/9d548ee0d08efa18/v1/staff_mm_westchester_instructors.json'
    return my_getCdnJson(staffCdnUrl)

##################################################################





