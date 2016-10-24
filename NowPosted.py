#Importing flask variables for a server side application
from flask import Flask, request, redirect, session

#Importing APIs/Libs
from twilio.rest import TwilioRestClient #Twilio
import twilio.twiml #Twilio
from indeed import IndeedClient #Indeed

#Importing the credentials for the various APIs and libs used
import credentials

#import userInfo

#For json parsing and creation if we need it
import json

#Imports for time based scheduling
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


app = Flask(__name__)
app.config.from_object(__name__)


#Creating the clients to interact with the APIs
twilio_api = TwilioRestClient(credentials.my_twilio_account_sid, credentials.my_twilio_auth_token)
indeed_api = IndeedClient(publisher = credentials.my_indeed_publisher_id)

def print_date_time(string, string2):
    #first string
    print("first parameter " + string)
    #second string
    print("second parameter " + string2)
    return None

def FindJobs(user_number):
    # query_param = userInfo['users'][user_number]['query']
    params = {
        'v': "2",
        'userip': "", #this might be a little tough to circumvent, maybe pull data from the form when signing up for NowPosted?
        'useragent': "", #use my own computers credentials?
        'q': "" #query_param
    }
    indeed_response = IndeedClient.search(**params)
    #old_jobs = userInfo['users'][user_number]['old_jobs']
    #loop that checks if any of the 50 new results for indeed exist in the old jobs array. if they do, remove from the json response
    #new_results = newest results from indeed search
    #return new_results

#some loop that creates time synced queueing ()
#for every phone number in clientele array
#FindJobs(user_number)
#make the request with the parameters from the "database"
#for every existing job for this phone number, eliminate from the search to have only 10 show up

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(func=print_date_time, trigger=IntervalTrigger(seconds=5), args=['string1','string2'], id='printing_job', name='Print date and time every five seconds', replace_existing=True)
atexit.register(lambda: scheduler.shutdown())

@app.route("/", methods=['GET', 'POST'])
def DeliverJobs():
    if request.method == 'GET':
        #return the website with the signup form
        print("get request made")
        return ""
    elif request.method == 'POST':
        #get form data from request object and place into a dict
        #attach to the json file http://stackoverflow.com/questions/23111625/how-to-add-a-key-value-to-json-data-retrieved-from-a-file-with-python
        return ""

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
