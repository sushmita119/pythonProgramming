from com.thoughtworks.tracker2.InputParser import *
from com.thoughtworks.tracker2.Tracker import *


class OutputPrinter:

    @classmethod
    def print_spending(cls, increased_item_prices_list):
        for item, (increased_price, first_month, percent) in increased_item_prices_list.items():
            print("Spending on " + item + " increased by " + "(" + str(increased_price) + "/" +
                  str(first_month) + " * " + str(100) + ")" + " " + str(int(percent)) + " percent")


if __name__ == "__main__":
    list_of_expense_category = InputParser().user_input()
    track = Tracker()
    increased_item_prices_list = track.expenditure_price(list_of_expense_category)
    OutputPrinter().print_spending(increased_item_prices_list)
'''
Package = 1
Classes = 1
Responsibility Segregation = 1
Explanation = 1
Questions 
Learnability = 1



'''