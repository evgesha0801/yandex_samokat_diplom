# Евгения Удальцова, 11-й поток — Финальный проект Яндекс Самокат. Инженер по тестированию плюс
import sender_stand_request
import data


def test_new_order():
    response = sender_stand_request.post_new_order(data.order_body)
    assert response.status_code == 201

def test_save_track():
    TRACK = sender_stand_request.post_new_order(data.order_body).json()["track"]
    return TRACK
def test_take_order():
    response = sender_stand_request.get_order(sender_stand_request.TRACK)
    assert response.status_code == 200,'Недостаточно данных для поиска или заказ не найден'