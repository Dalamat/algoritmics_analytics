import requests
import envs
import json
import time

AMO_HOST = envs.amo_host
AMO_LOGIN = envs.amo_login
AMO_PASSWORD = envs.amo_password

REQUEST_URL=f"https://{AMO_HOST}/settings/"
AUTH_URL = f"https://{AMO_HOST}/oauth2/authorize"
PIPELINES_URL = f"https://{AMO_HOST}/ajax/leads/list/"
EXPORT_URL = f"https://{AMO_HOST}/ajax/leads/export/"

def extract_csrf_token(response):
    var_start_index = response.find('csrf_token')
    value_start_index = response.find('value=', var_start_index)
    csrf_start_index = response.find('"', value_start_index)
    csrf_end_index = response.find('"', csrf_start_index + 1)
    return response[csrf_start_index + 1 : csrf_end_index]


def create_session_and_url():
    # Get the initial response to collect crsf_token
    session = requests.Session()
    url = REQUEST_URL
    response = session.get(url).text
    CSRF_TOKEN = extract_csrf_token(response)

    # Authenticate
    payload = {
        "csrf_token": CSRF_TOKEN,
        "username": AMO_LOGIN,
        "password": AMO_PASSWORD,
        "temporary_auth": "N",
    }
    url = AUTH_URL
    response = session.post(url, json=payload)
    
    # Get the list of pipelines
    headers = {'X-Requested-With': 'XMLHttpRequest'}
    response = session.post(PIPELINES_URL, headers=headers)
    pipelines_data = json.loads(response.text)
    pipelines_raw = pipelines_data['response']['pipelines']
    pipelines =  {p['id']: {i: q['id'] for i, q in enumerate(p['statuses'].values())} for p in pipelines_raw.values()}

    # Export data
    url = EXPORT_URL
    payload = {"encoding": "", "filter": {}, "type": "csv"}
    payload['filter'] = {
        'pipe': pipelines,
        'useFilter': 'y',
    }
    response = session.post(url, json=payload, headers=headers)
    # print(response.json())
    uuid = response.json()['uuid']
    # print(uuid)
    while True:
        time.sleep(10)
        response = session.get(url, headers=headers)
        status = (response.json())['status']
        print(status)
        if status['error_code']:
            raise Exception(status['error_code'])
        if status['progress'] == 100:
            break
    download_url = f"https://{AMO_HOST}/download/export/{uuid}"
    # print(download_url)
    return session, download_url

# login()