from address import Address
from mailing import Mailing


to_address = Address("633210", "г. Новосибирск", "ул. Тихая", "3", "15")
from_address = Address("633215", "г. Бердск", "ул. Комсомольская", "24", "136")

mailing = Mailing(to_address = to_address, from_address = from_address, cost = 450.00, track = "JP56987456")

track_info = f"Отправление {mailing.track} из "
from_info = f"{mailing.from_address} в "
to_info = f"{mailing.to_address}."
cost_info = f" Стоимость {mailing.cost} рублей"

print(track_info + from_info + to_info + cost_info)