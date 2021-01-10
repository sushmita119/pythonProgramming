from OOPS.hotelManagement.hotel import *


class Branch:

    def __init__(self, list_of_cus_details):
        self.hotels_name = [
            Hotel("Lakewood", 3, 110, 95, 80, 80),
            Hotel("Bridgewood", 4, 160, 60, 110, 50),
            Hotel("Ridgewood", 5, 220, 180, 100, 40)]
        self.list_of_cus_details = list_of_cus_details

    def suggestion(self):
        hotels_details = {}
        max_rating = 0
        min_price = 2147483647
        cheapest_hotel_names = []
        for customer in self.list_of_cus_details:
            for hotel in self.hotels_name:

                if customer.cus_type == "Regular":
                    hotel_price = hotel.regular_total_weekday_price(customer.no_of_weekdays) + \
                                  hotel.regular_total_weekend_price(customer.no_of_weekends)

                    hotels_details[hotel_price] = [hotel.name, hotel.rating]
                elif customer.cus_type == "Rewards":
                    hotel_price = hotel.reward_customer_weekday_price(customer.no_of_weekdays) + \
                                  hotel.reward_customer_weekend_price(customer.no_of_weekends)

                    hotels_details[hotel_price] = [hotel.name, hotel.rating]

            min_price = min(hotels_details)
            max_rating = hotels_details[min_price][1]
            for price, (name, rate) in hotels_details.items():
                if rate >= max_rating and price <= min_price:
                    cheapest_hotel_names.append(name)
        return cheapest_hotel_names

    def print_cheapest_hotel_name(self):
        names = self.suggestion()
        for name in names:
            print(name)