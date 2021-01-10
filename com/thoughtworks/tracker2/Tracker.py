from com.thoughtworks.tracker2.InputParser import *


class Tracker:
    @staticmethod
    def expenditure_price(list_of_expenses_category):
        increased_item_price_list = {}
        for item, price in list_of_expenses_category.items():
            first_month = price[0]
            if first_month > 0:
                for cost in range(1, len(price)):
                    increased_amount = price[cost] - first_month
                    percent = (increased_amount / first_month) * 100
                    if percent >= 125:
                        increased_item_price_list[item] = [increased_amount, first_month, percent]
        return increased_item_price_list
