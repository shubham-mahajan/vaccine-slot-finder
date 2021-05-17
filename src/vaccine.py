import requests, json, os
from notify import Notification

date = os.getenv('START_DATE')


def fetch(url):
    headers = {'Host':'cdn-api.co-vin.in', 'Accept':'application/json', 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15','Referer':'https://www.cowin.gov.in/'}
    return requests.get(url, headers=headers)

def fetch_by_pincode():
    '''Method to fetch on the basis of pincode'''
    pincodes = os.getenv('PINCODE').split(',')
    for pincode in pincodes:
        url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={date}'
        res = fetch(url)
        if res.status_code == 200:
            check_sesssion(res.json())

def fetch_districts():
    '''Method to fetch on the basis of discrict code'''
    districts = os.getenv('DISTRICTS').split(',')
    for district in districts:
        url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=213&date=17-05-2021'
        res = fetch(url)
        if res.status_code == 200:
            check_sesssion(res.json())


def check_sesssion(res):
    '''Method to check the presence of session and send notifications'''
    for center in res.get('centers'):
        for session in center.get('sessions'):
            if session.get('min_age_limit') >= int(os.getenv('MIN_AGE')) and \
                session.get('min_age_limit') <= int(os.getenv('MAX_AGE'))  and \
                session.get('date') >= date and \
                session.get('available_capacity') > int(os.getenv('MIN_REQUIRED')):
                message = f"Location - {center.get('district_name')} - {center.get('name')} {session.get('date')} - slots available {session.get('available_capacity')}"
                Notification().get_notification_channel_and_send(message)


if __name__ == '__main__':
    if os.getenv('DISTRICTS'):
        fetch_districts()
    if os.getenv('PINCODE'):
        fetch_by_pincode()