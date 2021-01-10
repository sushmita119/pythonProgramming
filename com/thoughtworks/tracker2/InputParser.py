class InputParser:
    list_of_expense_category = {"Personal care": [], "Entertainment": [], "Food": [], "Education": []}
    num_of_months = int(input("Enter the number of month"))

    @classmethod
    def user_input(cls):
        cls.initialize_list_of_expenses()
        for month in range(cls.num_of_months):
            month_no = int(input("Entries for month: "))
            while True:
                category = int(input("select category: 0.Exit 1.Personal care 2.Entertainment 3.Food 4.Education "))
                if category ==0:
                    break
                if category == 1:
                    expense = int(input("Personal care: "))
                    cls.list_of_expense_category["Personal care"][month_no-1] += expense
                elif category == 2:
                    expense = int(input("Entertainment: "))
                    cls.list_of_expense_category["Entertainment"][month_no-1] += expense
                elif category == 3:
                    expense = int(input("Food: "))
                    cls.list_of_expense_category["Food"][month_no-1] += expense
                elif category == 4:
                    expense = int(input("Education: "))
                    cls.list_of_expense_category["Education"][month_no-1] += expense
        return cls.list_of_expense_category

    @classmethod
    def initialize_list_of_expenses(cls):
        for index, value in cls.list_of_expense_category.items():
            for months in range(cls.num_of_months):
                value.append(0)


'''
Input Format
category = int(input("select category: 1.Personal care 2.Entertainment 3.Food 4.Education "))
                if not category:
                    break
                if category ==1:
                    entry = int(input("Personal care: "))
                    cls.list_of_expense_category["Personal care"] += entry
                elif category == 2:
                    entry = int(input("Entertainment: "))
                    cls.list_of_expense_category["Entertainment"] += entry
                elif category == 3:
                    entry = int(input("Food: "))
                    cls.list_of_expense_category["Food"] += entry
                elif category == 4:
                    entry = int(input("Education: "))
                    cls.list_of_expense_category["Education"] += entry

<number of months>

<category> <Amount>
<category> <Amount>

Sample Input
2 

Entries for the month: 1

“Personal care” 500
“Entertainment” 400
“Food” 400
“Personal care” 300

Entries for month 2:

“Food” 300
“Education” 200
“Entertainment” 900


Sample Output

Spending on Entertainment increased by (500/400 * 100)  125 percent


Feedback
1: Complex Input
Input : No of month
3
list_of_expense_category = {"Personal care": [0], "Entertainment": [0], "Food": [0], "Education": [0]}
"Personal care" : [0,0,0]
------------------------
Entry for month 2
list of predefined categories = 0 
for i in list
  value = input(i)
  list_of_expense_category.i.index(2,) += value
                for item,price in cls.list_of_expense_category.items():
                    entry = int(input("'"+item+"': "))
                    value[month_no] = 

'''
