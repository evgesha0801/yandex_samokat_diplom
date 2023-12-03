# Евгения Удальцова, 11-й поток — Финальный проект Яндекс Самокат. Инженер по тестированию плюс
import sender_stand_request

def test_take_response():
    assert sender_stand_request.take_order.status_code == 200,'Недостаточно данных для поиска или заказ не найден'