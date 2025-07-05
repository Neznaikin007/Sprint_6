import random
from data import DataForGenerators


class Generators:

    def generate_first_name(self):
        first_name = random.choice(DataForGenerators.first_name_list)
        return first_name

    def generate_last_name(self):
        last_name = random.choice(DataForGenerators.last_name_list)
        return last_name

    def generate_address(self):
        address = random.choice(DataForGenerators.address_list)
        return address

    def generate_metro_station(self):
        metro_station = random.choice(DataForGenerators.station_name)
        return metro_station

    def generate_comment(self):
        comment = random.choice(DataForGenerators.comment_list)
        return comment

    def generate_phone_number(self):
        phone_number = random.randint(1000000000, 9999999999)
        return f'+7{phone_number}'

    def generate_delivery_date(self):
        delivery_date = random.choice(DataForGenerators.delivery_date)
        return delivery_date

    def generate_scooter_color(self):
        scooter_color = random.choice(DataForGenerators.scooter_color)
        return scooter_color
