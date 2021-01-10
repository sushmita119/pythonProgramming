from OOPS.hotelManagement.InputParser import *
from OOPS.hotelManagement.branch import *
if __name__ == "__main__":
    list_of_details = InputParser().parse_input()
    branch = Branch(list_of_details)
    branch.print_cheapest_hotel_name()

'''
Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)
'''