from urllib.parse import urljoin

import requests
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

    """def get_token(self):
        location = 'pages/index/'
        headers = self._request('GET', location, json=False).headers
        return headers['Set-Cookie'].split(';')[0].split('=')[-1]"""

    def auth(self):
        url = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'

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
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        response = self.session.request('POST', url, headers=headers, data=data)

        if response.status_code == 302:
            location = response.headers['Location']
            response = self.session.request('GET', location)
        else:
            raise RequestErrorException(f' Got {response.status_code} {response.reason} for URL "{url}"')
        return response

"""
    def get_feed(self, feed_type='my'):
        location = 'feed/update/stream/'
        params = {'type': feed_type}

        return self._request('GET', location, params=params)

    def post_topic(self, title, text, blog_id=299, publish=True):
        location = 'blog/topic/create/'

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        data = {
            'csrfmiddlewaretoken': self.csrf_token,
            'title': title,
            'text': text,
            'blog': blog_id,
            'publish': 'on' if publish else ''
        }
        return self._request('POST', location, headers=headers, data=data)

    def delete_topic(self, topic_id):
        location = f'blog/topic/delete/{topic_id}/'

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        data = {
            'csrfmiddlewaretoken': self.csrf_token,
            'submit': 'Удалить',
        }
        return self._request('POST', location, headers=headers, data=data, json=False)
"""