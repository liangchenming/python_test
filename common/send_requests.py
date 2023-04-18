import requests
from requests.auth import HTTPBasicAuth

class SendRequests:
    sess = requests.Session()

    def all_send_requests(self, method, url, **kwargs):
        res = SendRequests.sess.request(method, url, auth=HTTPBasicAuth('user', 'dqwR5,2c.qdaeyq3oL'), **kwargs)
        return res
