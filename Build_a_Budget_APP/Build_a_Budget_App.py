class Category:
    def __init__ (self, name ):
        self.name = name 
        self.ledger = []

    def deposit(self, amount , description=""):
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        total = sum(item["amount"] for item in self.ledger)
        return total >= amount

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def transfer(self, amount, destination_category):
        if self.withdraw(amount, f"Transfer to {destination_category.name}"):
            destination_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            description = item['description'][:23]
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    spent_amounts = [-sum(item["amount"] for item in category.ledger if item["amount"] < 0) for category in categories]
    total_spent = sum(spent_amounts)
    spent_percentages = [(amount / total_spent * 100 // 10) * 10 if total_spent > 0 else 0 for amount in spent_amounts]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percentage in spent_percentages:
            chart += " o " if percentage >= i else "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    categories_names = [category.name for category in categories]
    max_length = max(len(name) for name in categories_names)
    for i in range(max_length):
        chart += "     "
        for name in categories_names:
            chart += f"{name[i] if i < len(name) else ' '}  "
        chart += "\n"

    return chart.rstrip("\n")



food = Category("Food")
food.deposit(100)
food.withdraw(10)

clothing = Category("Clothing")
clothing.deposit(100)
clothing.withdraw(30)


print(create_spend_chart([food, clothing]))
