from urllib import request
import json

###NOTE###
#It will take some time to reach open notify so be patient#

#URL variable - it will take some time to access the API
URL = "http://api.open-notify.org/astros.json"

#Function and i have to increase the timeout time because it took a while to reach the API
def total_people_space():
    access = request.urlopen(URL,timeout=50)
    response = json.loads(access.read())
    return f"There is/are total of {response['number']}"



    