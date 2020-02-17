from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
configuration = swagger_client.Configuration()
configuration.access_token = ''

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi(swagger_client.ApiClient(configuration))

def get_activity(id):
    try:
        # Get Activity
        api_response = api_instance.get_activity_by_id(id, include_all_efforts="false")
        return api_response
    except ApiException as e:
        print("Exception when calling ActivitiesApi->getActivityById: %s\n" % e)

def get_activity_list():
    activities = api_instance.get_logged_in_athlete_activities(before=1581811200,page=1,per_page=60,after=1578787200)
    return activities

def change_followers(activity_id, activity_details):
    import requests

    headers = {
        'authority': 'www.strava.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'origin': 'https://www.strava.com',
        'upgrade-insecure-requests': '1',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'referer': 'https://www.strava.com/activities/' + str(activity_id) + '/edit',
        'cookie': 'session_identifier=; _strava4_session=;',
    }

    data = [
        ('utf8', '\u2713'),
        ('_method', 'patch'),
        ('authenticity_token',
         ''),
        ('activity[name]', activity_details.name),
        # ('activity[description]', activity_details.description),
        ('activity[perceived_exertion]', ''),
        ('activity[visibility]', 'only_me'),
        ('activity[type]', 'Ride'),
        ('activity[workout_type]', '10'),
        ('activity[commute]', '0'),
        ('activity[commute]', '1'),
        ('activity[trainer]', '0'),
        ('activity[bike_id]', activity_details.gear_id[1:]),
        # ('default_photo_id', ''),
        ('commit', 'Save'),
    ]

    response = requests.post('https://www.strava.com/activities/' + str(activity_id), headers=headers, data=data)
    pprint(response)


activities = get_activity_list()
for a in activities:
    print(a.id,a.name,a.gear_id)
    change_followers(a.id, a)
