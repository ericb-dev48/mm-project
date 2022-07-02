from fileinput import filename
import json
from operator import indexOf
import requests
from urllib.request import urlopen
import ast

def ud_getCdnJson(url):   
    # store the response of URL
    response = urlopen(url)
        
    # storing the JSON response
    # from url in data
    data_json = json.loads(response.read())
        
    return data_json

myData = ud_getCdnJson('https://cdn.baseboosters.com/9d548ee0d08efa18/v1/staff.json')

indexList = myData['records']
arrforyou = []

for record in myData['records']:
    myIndex = indexList.index(record)
    img_data = str((myData['records'][myIndex]['profile_img']))
    arrforyou.append(img_data)

for object in arrforyou:
    img_data = ast.literal_eval(object)


