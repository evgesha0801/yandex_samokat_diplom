import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

response = post_new_order(data.order_body);

TRACK = response.json()["track"]

take_order = requests.get(configuration.URL_SERVICE + configuration.TAKE_ORDER_TRACK, TRACK)
