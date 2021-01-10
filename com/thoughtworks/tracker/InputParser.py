class Input:
    list_of_expense_category = {"Personal care": [0], "Entertainment": [0], "Food": [0], "Education": [0]}
    num_of_months = int(input())

    @classmethod
    def parse_input(cls):
        count = -1
        for month in range(cls.num_of_months):
            count += 1

            month_no = int(input("Entries for month"))
            while True:
                entries = input()
                if not entries:
                    break
                category = cls.parse_category(entries)
                spending = cls.parse_spending(entries)
                for index, value in cls.list_of_expense_category.items():
                    if index == category:
                        value[count] = value[count] + spending

            for index, value in cls.list_of_expense_category.items():
                value.append(0)

        return cls.list_of_expense_category

    @classmethod
    def parse_category(cls, entry):
        digit_index = 0
        for character in entry:
            if character.isdigit():
                digit_index = entry.index(character)
                break
        category = entry[1:(digit_index - 2)]
        return category

    @classmethod
    def parse_spending(cls, entry):
        digit_index = 0
        for character in entry:
            if character.isdigit():
                digit_index = entry.index(character)
                break
        spending = entry[digit_index:]
        return int(spending)


'''
Input Format

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
  

'''
