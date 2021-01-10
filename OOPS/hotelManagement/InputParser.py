from OOPS.hotelManagement.customer import *


class InputParser:

    def parse_input(self):
        staying_details = []
        while True:
            customer_details = input()
            if not customer_details:
                break
            customer_type = self.parse_customer_type(customer_details)
            number_of_weekdays = self.parse_weekdays(customer_details)
            number_of_weekends = self.parse_weekends(customer_details)
            staying_details.append(Customer(customer_type, number_of_weekdays, number_of_weekends))
        return staying_details

    @staticmethod
    def parse_customer_type(customer_details):
        customer_type = customer_details.split(":")[0]
        return customer_type

    @staticmethod
    def parse_weekdays(customer_details):
        count = 0
        weekday = ["(mon)", "(tues)", "(wed)", "(thur)", "(fri)"]
        first_split = customer_details.split(" ")[1:]
        temp = ""
        temp = temp.join(first_split)
        temp = temp.split(",")
        days = []
        for curr_day in temp:
            day = curr_day[9:]
            days.append(day)
        for day in days:
            if day in weekday:
                count += 1
        return count

    @staticmethod
    def parse_weekends(customer_details):
        count = 0
        weekends = ["(sat)", "(sun)"]
        first_split = customer_details.split(" ")[1:]
        temp = ""
        temp = temp.join(first_split)
        temp = temp.split(",")
        days = []
        for curr_day in temp:
            day = curr_day[9:]
            days.append(day)
        for day in days:
            if day in weekends:
                count += 1
        return count