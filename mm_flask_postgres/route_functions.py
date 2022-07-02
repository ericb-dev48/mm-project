from http.client import SWITCHING_PROTOCOLS
from tokenize import maybe
from click import argument
import json

# import json
# from main_db import conn
# cur = conn.cursor()

# import psycopg2
# from main_db import conn
# Open a cursor to perform database operations
# cur = conn.cursor()

###########################################################

# def homeFunc():
#     staff_list = []
#     cur.execute("SELECT * from staff")
#     staff_data = cur.fetchall()
#     print("staff_data", staff_data)
#     for record in staff_data:
#         print(record)
#         staff_dict = {
#             "record_id":record[0], 
#             "last_name":record[1],
#             "first_name":record[2]}
#         staff_list.append(staff_dict)
#         print("staff_list: ", staff_list)
#     return render_template("stafflist2.html", staff_list = staff_list)

############################

############################

############################

### For About Us Page ###

def rf_getStaffList():

    staffJsonUrl = ""

    staff_data_json = ud_getCdnJson(staffJsonUrl)
    records = staff_data_json['records']
    staff_list = []

    for record in records:
        i = records.index(record)
        print(i)
        # img_url = record['profile_img'][0]['url']
        print(type(record['profile_img'][0]))
        
        job_title = record['position']
        for i in record['profile_img']
            print(i)


        staff_dict = {
            "bio": record['bio'],
            "staff_name": record['staff_name'],
            "position": job_title,
            # "profile_img": 
            # "profile_img": img_url
        }
        staff_list.append(staff_dict)
    
    return staff_list
    
    # return render_template("stafflist.html", staff_list_ret = staff_list_ret) 

############################



############################