import requests


class API:
    API_VERSION = 'v1'
    API_URL = 'api.liquiditi.io'

    def __init__(self, token):
        super(API, self).__init__()
        self.token = token

    def _request(self, action, method, params={}, data={}):
        r = requests.__dict__[action](**{
            'url': f'https://{self.API_URL}/{self.API_VERSION}/{method}/',
            'params': params,
            'json': data,
            'headers': {
                'Authorization': f'Token {self.token}'
            }
        })

        if r.status_code != 200:
            return {
                'error': r.status_code,
            }

        return r.json()

    def order_create(self, from_currency, to_currency, address):
        return self._request('post', 'order', data={
            'from_currency': from_currency,
            'to_currency': to_currency,
            'address': address,
        })

    def order_list(self, status=False):
        return self._request('get', 'order', params={'status': status})

    def order_get(self, order_id):
        return self._request('get', f'order/{order_id}')

    def currency_list(self, status=False):
        return self._request('get', 'currency')
