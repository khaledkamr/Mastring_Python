
def truncate(n):

    multiplier = 10
    return int(n * multiplier) / multiplier

def get_totals(categories):

    total = 0
    breakdown = []

    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())

    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded

def create_spend_chart(categories):
    
    print("Percentage spent by category")
    i = 100
    totals = get_totals(categories)

    while i >= 0:
        cat_space = ""

        for total in totals:
            if total * 100 >= i:
                cat_space += " o "
            else:
                cat_space += "   "
        
        print(str(i).rjust(3) + "|" + cat_space + ("\n"), end = "")
        i -= 10
    
    dashes = "-" + "---" * len(categories)
    names = []
    x_axis = ""

    for category in categories:
        names.append(category.name)

    maxi = max(names, key = len)

    for x in range(len(maxi)):

        nameStr = "     "

        for name in names:
            if x >= len(name):
                nameStr += "   "
            else:
                nameStr += name[x] + "  "
        
        if(x != len(maxi) - 1):
            nameStr += "\n"
        
        x_axis += nameStr
    
    print(dashes.rjust(len(dashes) + 4) + "\n" + x_axis)
    return ""

class Category:

    def __init__(self, name):

        self.name = name
        self.ledger = list()

    def __str__(self):

        ast = (30 - len(self.name))//2
        print("*" * ast, end = "")
        print(self.name, end = "")
        print("*" * ast)

        for item in self.ledger:

            print(f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}")
        
        return f"Total: {self.get_balance()}$"

    def deposit(self, amount, description = ""):

        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        
        if(self.check_funds(amount)):
            self.ledger.append({"amount": amount * -1, "description": description})
            return True
        else:
            return False
    
    def get_balance(self):

        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        
        return balance

    def transfer(self, amount, category):

        if(self.check_funds(amount)):
            self.withdraw(amount, f"transfer to {category.name}")
            category.deposit(amount, f"transfer from {self.name}")
            return True
        else:
            return False     
       
    def check_funds(self, amount):

        if(amount <= self.get_balance()):
            return True
        else:
            return False
    
    def get_withdrawls(self):

        total = 0

        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]

        return total

food = Category("food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")
clothing = Category("clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food,"\n")
print(clothing,"\n")
print(auto,"\n")

print(create_spend_chart([food, clothing, auto]))



