#https://github.com/fuzzyray/budget-app/blob/main/budget.py
class Category:
    def __init__(self,what): 
        self.ledger = [] 
        self.type = what
        self.currentBalance = 0

    def __repr__(self):
        str_name = self.type.center(30, "*") + "\n"
        str_others = ""
        for x in self.ledger:
            item_desc = "{:<23}".format(x["description"])
            item_amount = "{:>7.2f}".format(x["amount"])
            str_others += "{}{}\n".format(item_desc[:23], item_amount[:7])
        total = "Total: {:.2f}".format(self.currentBalance)
        return str_name + str_others + total

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount, "description": desc})
        self.currentBalance += amount

    def get_balance(self):
        return self.currentBalance

    def withdraw(self, amount, desc=""):
        if self.currentBalance - amount >= 0:
            self.ledger.append({"amount": -1 * amount, "description": desc})
            self.currentBalance -= amount
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if self.currentBalance >= amount:
            return True
        else:
            return False

    def transfer(self, amount, nextOne):
        if self.withdraw(amount, "Transfer to {}".format(nextOne.type)):
            nextOne.deposit(amount, "Transfer from {}".format(self.type))
            return True
        else:
            return False

def create_spend_chart(categories):
    amounts = []

    for eachCat in categories:
        spent = 0
        for x in eachCat.ledger:
            if x["amount"] < 0:
                spent += abs(x["amount"])
        amounts.append(round(spent, 2))

    total = 0
    for x in amounts:
      total += x
    total = round(total, 2)

    percentageAmount = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), amounts))

    hdr = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in percentageAmount:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.type, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (hdr + chart + footer).rstrip("\n")