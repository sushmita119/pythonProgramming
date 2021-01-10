from com.thoughtworks.tracker.InputParser import *
from com.thoughtworks.tracker.Tracker import *

if __name__ == "__main__":
    list_of_expenditure = Input().parse_input()
    track = Tracker()
    track.print_lis(list_of_expenditure)
