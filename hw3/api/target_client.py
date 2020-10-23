from urllib.parse import urljoin

import requests
import time
import json
from requests.cookies import cookiejar_from_dict


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class TargetClient:

    def __init__(self, email, password):
        self.base_url = 'https://target.my.com'

        self.session = requests.Session()
        self.csrf_token = None

        self.email = email
        self.password = password
        self.auth()

    def auth(self):
        url = 'https://auth-ac.my.com/auth'

        data = {
            'email': self.email,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1#email',
            'failure': 'https://account.my.com/login/'
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Referer': 'https://target.my.com/',
                   'Origin': 'https://target.my.com',
                   'Sec-Fetch-Dest': 'document',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
                   }
        response = self.session.request('POST', url, headers=headers, data=data,allow_redirects=False)

        if response.status_code == 302:
            location = response.headers['Location']
            response = self.session.request('GET', location)
        else:
            raise RequestErrorException(f' Got {response.status_code} {response.reason} for URL "{url}"')
        return response

    def get_token(self):
        location = 'https://target.my.com/csrf'
        response = self.session.request('GET', location)
        return response.headers['Set-Cookie'].split(';')[0].split('=')[-1]

    def seg_create(self):
        url = 'https://target.my.com/api/v2/remarketing/segments.json'

        headers = {'Content-Type': 'application/json',
                   'Referer': 'https://target.my.com/segments/segments_list/new',
                   'Origin': 'https://target.my.com',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
                   'X-CSRFToken': self.get_token(),
                   'X-Requested-With': 'XMLHttpRequest'}
        data = {
            'name': f'New segment {time.ctime()}',
            'pass_condition': 1,
            'logicType': "or",
            'relations': [
                {'object_type': "remarketing_player", 'params': {'type': "positive", 'left': 365, 'right': 0}}
            ]
        }

        return self.session.request('POST', url, headers=headers, data=json.dumps(data))

    def delete_segment(self):
        response = self.seg_create()

        id = response.json()['id']
        url = f'https://target.my.com/api/v2/remarketing/segments/{id}.json'
        headers = {'X-CSRFToken': self.get_token(),
                   'Referer': 'https://target.my.com/segments/segments_list'}
        response = self.session.request('DELETE', url, headers=headers)
        return response
