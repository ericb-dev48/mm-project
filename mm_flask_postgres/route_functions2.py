#Important function for accessing files from parent directory
import sys
import os

def appendParent():
    current = os.path.dirname(os.path.realpath(__file__))
    parent = os.path.dirname(current)
    sys.path.append(parent)
##############################################################

import json

def rf_getStaffList():

    staffJsonUrl = '/Users/ericberman/HQ/dev/musical_munchkins/mm_flask_postgres/airtable_json_data/mm_staff.json'

    with open(staffJsonUrl, 'r') as read_file:
        jsonData = json.load(read_file)
    
    return jsonData
