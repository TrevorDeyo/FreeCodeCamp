class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # When the budget object is printed it should display:
    # A title line of 30 characters where the name of the category
    # is centered in a line of * characters. A list of the items
    # in the ledger. Each line should show the description and
    # amount. The first 23 characters of the description should
    # be displayed, then the amount. The amount should be right
    # aligned, contain two decimal places, and display a maximum
    # of 7 characters. A line displaying the category total.
    def __str__(self):
        title_length = 30
        category_name = self.name.strip('*')

        title_line = f"{category_name.center(title_length, '*')}\n"

        items = ""
        total = 0

        for transaction in self.ledger:
            description = transaction["description"].replace('*', ' ')[:23].ljust(23)
            amount = "{:.2f}".format(transaction["amount"]).rjust(7)
            items += f"{description}{amount}\n"
            total += transaction["amount"]
        
        total_line = f"Total: {total:.2f}"

        return title_line + items + total_line.rstrip()

    # A deposit method that accepts an amount and description.
    # If no description is given, it should default to an empty
    # string. The method should append an object to the ledger
    # list in the form of {"amount": amount, "description": description}.
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    # A check_funds method that accepts an amount as an argument.
    # It returns False if the amount is greater than the balance
    # of the budget category and returns True otherwise. This method
    # should be used by both the withdraw method and transfer method.
    def check_funds(self, amount):
        total_balance = sum(transaction["amount"] for transaction in self.ledger)
        return total_balance >= amount

    # A withdraw method that is similar to the deposit method,
    # but the amount passed in should be stored in the ledger
    # as a negative number. If there are not enough funds, nothing
    # should be added to the ledger. This method should return True
    # if the withdrawal took place, and False otherwise.
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    # A get_balance method that returns the current balance of
    # the budget category based on the deposits and withdrawals
    # that have occurred.
    def get_balance(self):
        return sum(transaction["amount"] for transaction in self.ledger)
    
    # A transfer method that accepts an amount and another budget
    # category as arguments. The method should add a withdrawal
    # with the amount and the description "Transfer to [Destination
    # Budget Category]". The method should then add a deposit to
    # the other budget category with the amount and the description
    # "Transfer from [Source Budget Category]". If there are not
    # enough funds, nothing should be added to either ledgers. This
    # method should return True if the transfer took place,
    # and False otherwise.
    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            description_withdraw = f"Transfer to {destination_category.name}"
            description_deposit = f"Transfer from {self.name}"

            self.withdraw(amount, description_withdraw)
            destination_category.deposit(amount, description_deposit)
            return True
        else:
            return False
    
    def get_withdrawals(self):
        return sum(transaction["amount"] for transaction in self.ledger if transaction["amount"] < 0)

# create_spend_chart that takes a list of categories as an argument.
# It should return a string that is a bar chart. The chart should show
# the percentage spent in each category passed in to the function.
# The percentage spent should be calculated only with withdrawals and
# not with deposits. Down the left side of the chart should be labels
# 0 - 100. The "bars" in the bar chart should be made out of the "o"
# character. The height of each bar should be rounded down to the
# nearest 10. The horizontal line below the bars should go two spaces
# past the final bar. Each category name should be written vertically
# below the bar. There should be a title at the top that says
# "Percentage spent by category".

def truncate_decimal(number):
    decimal_multiplier = 10
    return int(number * decimal_multiplier) / decimal_multiplier

def calculate_totals(categories):
    total_amount = 0
    withdrawal_breakdown = []
    for category in categories:
        total_amount += category.get_withdrawals()
        withdrawal_breakdown.append(category.get_withdrawals())
    rounded_breakdown = list(map(lambda x: truncate_decimal(x / total_amount), withdrawal_breakdown))
    return rounded_breakdown

def calculate_category_percentage(category, total_amount):
    percentage = (category.get_withdrawals() / total_amount) * 100
    return int(percentage)

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    i = 100
    withdrawal_totals = calculate_totals(categories)
    while i >= 0:
        category_spaces = " "
        for total in withdrawal_totals:
            if total * 100 >= i:
                category_spaces += "o  "
            else:
                category_spaces += "   "
        chart += str(i).rjust(3) + "|" + category_spaces + ("\n")
        i -= 10

    dashes = "-" + "---" * len(categories)
    category_names = []
    x_axis = ""
    for category in categories:
        category_names.append(category.name)

    max_category_name_length = max(category_names, key=len)

    for x in range(len(max_category_name_length)):
        name_str = '     '
        for name in category_names:
            if x >= len(name):
                name_str += "   "
            else:
                name_str += name[x] + "  "

        if x != len(max_category_name_length) - 1:
            name_str += '\n'

        x_axis += name_str

    chart += dashes.rjust(len(dashes) + 4) + "\n" + x_axis
    return chart
