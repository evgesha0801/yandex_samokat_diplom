import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

TRACK_ORDER = post_new_order(data.order_body).json()["track"]

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TAKE_ORDER_TRACK + str(track))
