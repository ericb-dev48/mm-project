# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from re import X
from flask import Flask, render_template
from route_functions2 import rf_getStaffList
from airtable_cdn import my_getStaffCdnJson

#############################################

app = Flask(__name__)

#############################################

#Home page
@app.route('/')
def homeRouteFunc():
    return render_template('p_home.html')

##############################################

#About page
@app.route('/about')
def aboutRouteFunc(): 
    staffJson = my_getStaffCdnJson()
    staffRecords = staffJson['records']
    
    myString = ""

    for i in staffRecords:
        myString += i['full_name']
    
    # staff_list = rf_getStaffList()
    # print(staff_list)
    # print(type(staff_list))
    return render_template('p_about_cdn.html', staffRecords = staffRecords)
    # return myString



# @app.route('/about')
# def aboutRouteFunc(): 
#     staff_list = rf_getStaffList()
#     print(staff_list)
#     print(type(staff_list))
#     return render_template('p_about.html', staff_list = staff_list)

###############################################

#Our classes page
@app.route('/our-classes')
def ourClassesRouteFunc():
    return render_template('p_our_classes.html')

###############################################

#Schedule page
@app.route('/schedule')
def scheduleRouteFunc():
    return render_template('p_schedule.html')

###############################################

#Schedule page
@app.route('/locations')
def locationsRouteFunc():
    return render_template('p_locations.html')

###############################################

#Register page
@app.route('/register')
def registerRouteFunc():
    return render_template('p_register.html')

###############################################

#Covid protocols page
@app.route('/covid-protocols')
def covidRouteFunc():
    return render_template('p_covid_19_protocols.html')

###############################################

#Parties page
@app.route('/parties')
def partiesRouteFunc():
    return render_template('p_parties.html')

###############################################

#partnerships page
@app.route('/partner-with-us')
def partnerRouteFunc():
    return render_template('p_partner_with_us.html')

###############################################

#partnerships page
@app.route('/teacher-training')
def teacherTrainingRouteFunc():
    return render_template('p_teacher_training.html')

###############################################


# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='127.0.0.1',port=8000,debug=True)