
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
        
        return f"Total: {self.get_balance()} $"

    def deposit(self, amount, description = ""):

        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        
        if(self.check_funds(amount)):
            self.ledger.append({"amount": amount*-1, "description": description})
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


