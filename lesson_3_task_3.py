from address import Address
from mailing import Mailing

to_address = ("633210, г. Новосибирск, ул. Тихая, 3 - 15")
from_address = ("633215, г. Бердск, ул. Комсомольская, 24 - 136")
track = ("JP56987456") 
cost = ("450.00 рублей")

print(f"Отправление: {track} из {from_address} в {to_address}. Стоимость {cost}.")