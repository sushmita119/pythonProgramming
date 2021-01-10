class Tracker:

    def __init__(self, total_expenditure):
        self.total_expenditure = total_expenditure

    def expenditure_price(self):
        increased_item_price_list = []
        for item, price_list in self.total_expenditure.items():
            price_list[:] = (value for value in price_list if value != 0)
            if len(price_list) > 1:
                first_month = price_list[0]
                for price in range(1, len(price_list)):
                    percent = ((price_list[price] - first_month) / first_month) * 100
                    if percent >= 125:
                        increased_item_price_list.append("Spending on " + item + " increased"
                                                                                 " by " + "(" + str(
                            (price_list[price] - first_month)) + "/" + str(first_month) + " * "
                                                                                          "" + str(
                            100) + ")" + " " + str(int(percent)) + " percent")
        return increased_item_price_list

    def print_lis(self):
        tracker_list = self.expenditure_price()
        for item in tracker_list:
            print(item)



